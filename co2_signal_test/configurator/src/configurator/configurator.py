import copy
import json
import logging
from typing import Any, Optional, Union

from . import config
from . import periodical_job
from . import referee
from . import source

# logging will be from name of the module for all submodules.
# if you want to change logging setting you should work with this semi global variable.
CONFIGURATOR_LOGGER: logging.Logger = logging.getLogger(__name__)
config.CONFIGURATOR_LOGGER = CONFIGURATOR_LOGGER
source.CONFIGURATOR_LOGGER = CONFIGURATOR_LOGGER
periodical_job.CONFIGURATOR_LOGGER = CONFIGURATOR_LOGGER
referee.CONFIGURATOR_LOGGER = CONFIGURATOR_LOGGER


class Configurator(config.Config):
    # Class - facade for the module. Combines all elements and interfaces.
    def __new__(cls, name: Optional[str], **kwargs):
        instance: Configurator
        configs_referee = referee.Referee()

        if configs_referee.is_configurator_exists(configurator_name=name):
            message = f'Configurator exists, we will use it {name=}.'
            CONFIGURATOR_LOGGER.debug(message)
            instance = configs_referee.get_configurator(name)
            if not instance:
                message = f'Config should exists {instance=}, {name=} but it is not'
                raise ValueError(message)
        else:
            instance = super().__new__(cls)
            message = f'Creating new configurator {name=}.'
            CONFIGURATOR_LOGGER.debug(message)

        return instance

    def __init__(self, name: Optional[str], **kwargs):
        # {'name': 'logger config',
        #  'parameters': {'force': True, },
        #  'sources': [{'path': r'C:\Users\admin\PycharmProjects\config_keeper\src\configs\my_config.json'}, ],
        #  'periodical_jobs': [],
        #  'config': {}}
        FORCE = False
        configs_referee = referee.Referee()

        if hasattr(self, 'initialized'):
            # skip init
            pass
        else:
            self.initialized = False
            self.configs_referee = referee.Referee()
            # name can be none if init happens from source. name will be updated from sources
            self.name: Optional[str] = name
            self.version: Optional[float] = None

            self.sources = {}
            self.periodical_jobs = {}

            self.do_init(name, **kwargs)
            self.initialized = True

        # If after initialization, config doesn't have unic name. Something went wrong.
        if not self.name:
            # TODO implement "force" parameter
            message = f'Configurator did not get a name. If it was your plan use "force" (not implemented)'
            CONFIGURATOR_LOGGER.error(message)
            if not FORCE:
                # configs_referee is singleton. It should be done otherwise failed configurators stay.
                configs_referee.remove_configurator(self.name)
                del self
                raise ValueError(message)
        # add an object to referee
        elif not configs_referee.is_configurator_exists(configurator_name=self.name):
            configs_referee.add_configurator(self)

    def do_init(self, name: Optional[str], **kwargs):
        # prepare args for super instance. may be this part should be changed in the future
        kwargs_for_super = {}
        if 'default' in kwargs:
            kwargs_for_super['default'] = kwargs['default']
        if 'create_if_not_exists' in kwargs:
            kwargs_for_super['create_if_not_exists'] = kwargs['create_if_not_exists']
        super().__init__(**kwargs_for_super)

        self.add_sources(kwargs.pop('sources', None))

        periodical_jobs: dict = kwargs.pop('periodical_jobs', {})
        if periodical_jobs:
            for source_id, periodical_jobs_init_params in periodical_jobs:
                # TODO add init for periodical jobs
                self.periodical_jobs[source_id].append(None)

        self.update_configurator()

    def remove_configurator(self):
        self.configs_referee.remove_configurator(self.name)

    def is_configurator_exists(self) -> bool:
        exists = self.configs_referee.is_configurator_exists(self.name)
        return exists

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # name setter can be called before __init__ configs_referee will be not created
        self._name = name
        self.configs_referee.name_changed(self)

    def __eq__(self, other):
        is_equal = False
        my_dict = self.__to_dict()
        other_dict = other.__to_dict()

        if my_dict == other_dict:
            is_equal = True

        return is_equal

    def add_sources(self, input_sources: Union[dict, source.Source, list, None]):
        """Transform configurator to dict format
        @param input_sources Dictionary or Source/s object/s."""

        prepared_sources = {}
        if isinstance(input_sources, dict):
            # sources are in dictionary with ids as keys
            # check that all keys are int if not raise error
            for key in input_sources.keys():
                try:
                    int(key)
                except ValueError:
                    message = f'One of the keys is not int in sources(can not be casted to int) {input_sources.keys()=}'
                    raise TypeError(message)

            # JSON standard allows dictionary keys strings only!
            if all(isinstance(int(key), int) for key in input_sources.keys()):
                for source_id, source_params in input_sources.items():
                    prepared_sources[int(source_id)] = self.source_fabric(**source_params)
            # source is in dictionary
            elif all(isinstance(key, str) for key in input_sources.keys()):
                # TODO not implemented
                pass
            else:
                message = f'Not expected info for source creation'
                raise ValueError(message)
        elif isinstance(input_sources, source.Source):
            # TODO not implemented
            pass
        elif isinstance(input_sources, list):
            # TODO not implemented
            pass
        elif not input_sources:
            # can be None and it is ok.
            pass
        else:
            message = f'not expected type: "{type(input_sources)}" of a source: "{input_sources}". Should be dict or source object'
            raise TypeError(message)

        # Add sources from prepared dict
        for source_id, source_obj in prepared_sources.items():
            self.add_source(input_source=source_obj, source_id=source_id)

    def add_source(self, input_source: source.Source, source_id: Optional[int] = None):
        """Add source to configurator.
        @param input_source which should be used to update all properties of the configurator
        @param source_id id for the source. If source id None or not defined,
                        id should be created as autoincrement after the last id in the configurator.
                        ID should not be less than 1 and should be int.
        """
        if not isinstance(input_source, source.Source):
            message = f'Input {input_source=} is not source object type'
            raise TypeError(message)
        if not (isinstance(source_id, int) or (source_id is None)):
            message = f'Source {source_id=} is not INT type'
            raise TypeError(message)

        if source_id is None:
            if self.sources.keys():
                max_id = max(self.sources.keys())
                source_id = max_id + 1
            else:
                source_id = 1
        elif source_id < 1:
            message = f'Source {source_id=} is less than 1'
            raise ValueError(message)
        elif source_id >= 1:
            # Normal case. Nothing to do.
            pass
        else:
            # Safe part. If this part is interpreted, something went wrong and block has errors in conditions.
            message = f'Should not be run.'
            raise RuntimeError(message)

        self.sources[source_id] = input_source

    def is_source_exist(self, source_id: int) -> bool:
        """Checks if the source exists or not.

        @param source_id ID of the source which should be checked.

        @return Return True if source exists otherwise False."""
        source_exists = source_id in self.sources.keys()
        return source_exists

    def get_sources(self) -> dict:
        """Provide all sources in dictionary format.

        @return Return sources."""
        return self.sources

    def delete_source(self, source_id: int) -> bool:
        """Delete source bie it ID

        @param source_id ID of the source which should be deleted from the configurator.

        @return Return True if successful otherwise raise error."""

        if self.is_source_exist(source_id):
            self.sources.pop(source_id)
            self.update_configurator()
        else:
            message = f'Incorrect source ID for deletion'
            raise ValueError(message)
        return True

    def __to_dict(self) -> dict:
        """Transform configurator to dict format
        @return Dictionary representation of configurator."""

        sources = {}
        if self.sources:
            for key, source_inc in self.sources.items():
                sources[key] = source_inc.to_dict()
        jobs = {}
        if self.periodical_jobs:
            for key, job in self.periodical_jobs.items():
                jobs[key] = job.to_dict()

        return_value = {'data': copy.deepcopy(self._data),
                        'name': self.name,
                        'version': self.version,
                        'sources': sources,
                        'periodical_jobs': jobs
                        }
        return return_value

    def __from_dict(self, input_dictionary: dict):
        """Transform configurator to dict format
        @param Dictionary which should be used to update all properties of the configurator
        """
        config_data = copy.deepcopy(input_dictionary.pop('data', None))
        if config_data:
            self.load_config(config_data)

        self.add_sources(input_dictionary.pop('sources', {}))
        # TODO do restore for periodical jobs

        # assign all existed parameters from config to object
        # TODO check which parameters are not presented in input and notify
        for param_name, value in input_dictionary.items():
            if hasattr(self, param_name) and getattr(self, param_name) != value:
                setattr(self, param_name, value)
            else:
                message = f'Input parameter name "{param_name}" with value "{value}" is not defined in configurator and will be ignored'
                CONFIGURATOR_LOGGER.debug(message)

    def __str__(self):
        """Transform configurator to dict format

        @return Dictionary representation of configurator."""
        output: str
        output = json.dumps(self.__to_dict(), indent=4)
        return output

    def change_version_deco(self, method):
        def wrapper(self, *args):
            self.version += 0.1
            method(self)

        return wrapper
        # print(self.version)

    # override config interface methods
    def get_parameter(self, parameter_name: str, **kwargs) -> Any:
        """Constructor creates config object
        @param: self The object pointer.
        @param: parameter_name The name of the parameter key.
        @param: default Return this value if the parameter is not exists.
        @return:
        """
        value = super().get_parameter(parameter_name=parameter_name, **kwargs)
        return value

    def add_parameter(self, parameter_name: str, value: Any, force: bool = True) -> None:
        """

        @return
        """
        super().add_parameter(parameter_name=parameter_name, value=value)

    def update_parameter(self, parameter_name: str, value: Any) -> None:
        """

        @return
        """
        super().update_parameter(parameter_name=parameter_name, value=value)

    def delete_parameter(self, parameter_name: str):
        """

        @return
        """
        super().delete_parameter(parameter_name=parameter_name)

    # override config source interface methods

    def update_configurator(self):
        # load from all sources
        # define the newest
        # update configurator from it
        # TODO priority should be implemented
        for source_id, source_obj in self.sources.items():
            self.__from_dict(source_obj.get_config())

        self.save_configurator()

    def save_configurator(self):
        for source_obj in self.sources.values():
            source_obj.save_config(self.__to_dict())

    @staticmethod
    def source_fabric(**kwargs) -> source.Source:
        """Create a source object
        @param: cls Class pointer.

        @param: Source_type str. Defines in direct way which type of source should be created.
        @param: path str or pathlike object. Can be path to file/subdir or full path with file name. If blank, current dir will be taken
        @param: subdir str or pathlike object. Adds to the path if not blank and path not absolute.
        @param: file_name str. Adds to the end if the path is not full. Extension defines the type of source if the type is not presented.
        @return: Source object
        """
        new_source = source.SourceFabric.create_source(**kwargs)
        return new_source

    @classmethod
    def from_file(cls, file_name: str = '', file_subdir: str = '', file_path: str = '') -> 'Configurator':
        config_init_params = {'sources': {1: {'file_name': file_name,
                                              'subdir': file_subdir,
                                              'path': file_path}
                                          }
                              }
        new_configurator = cls(name=None, **config_init_params)
        # If name for the configurator was not updated from source. Creation will be not successful
        return new_configurator

    @classmethod
    def from_variable(cls, variable: dict) -> 'Configurator':
        """Create config object form dictionary variable

        @param variable from which object should be created.

        @return Config object."""
        # TODO not implemented
        raise NotImplementedError()


if __name__ == "__main__":
    pass
