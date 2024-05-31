import abc
import json
import logging
import pathlib

CONFIGURATOR_LOGGER: logging.Logger


class SourceInterface(abc.ABC):
    @abc.abstractmethod
    def get_config(self) -> dict:
        pass

    @abc.abstractmethod
    def save_config(self, data: dict) -> None:
        pass

    @abc.abstractmethod
    def to_dict(self) -> dict:
        pass


class SourceFabric:
    def __init__(self):
        message = f'SourceFabric should not have instance'
        raise NotImplementedError(message)

    @classmethod
    def create_source(cls, **kwargs) -> 'Source':
        source = None
        if ('path' in kwargs) or ('file_name' in kwargs):
            source = cls.__create_file_source(**kwargs)
        elif 'url' in kwargs:
            # TODO not implemented
            message = f'Source fabric did not create correct source: "{source}". Input was: {kwargs}'
            raise NotImplementedError(message)
        elif 'variable' in kwargs:
            # TODO not implemented
            message = f'Source fabric did not create correct source: "{source}". Input was: {kwargs}'
            raise NotImplementedError(message)
        else:
            message = f'Not expected input for source creation {kwargs=}'
            raise ValueError(message)

        if not isinstance(source, Source):
            message = f'Source fabric did not create correct source: "{source}". Input was: {kwargs}'
            raise ValueError(message)

        # if user defined priority for a created source, it will be assigned to internal source properties
        if kwargs.get('priority'):
            source.priority = kwargs.get('priority')
        return source

    @classmethod
    def __create_file_source(cls, **kwargs) -> 'Source':
        config_path = pathlib.Path()
        if 'path' in kwargs:
            input_path = kwargs.get('path')
            if isinstance(input_path, str):
                config_path = config_path / input_path
            else:
                message = f'Path variable is {type(input_path)} which not allowed. Should be string.'
                raise ValueError(message)
        else:
            config_path = config_path / pathlib.Path.cwd()

        if 'subdir' in kwargs:
            config_path = config_path / kwargs['subdir']

        if 'file_name' in kwargs:
            config_path = config_path / kwargs['file_name']

        source_type = None
        if 'source_type' in kwargs:
            source_type = kwargs['source_type']

        if (source_type == 'json file') or (config_path.suffix == '.json'):
            source = SourceJsonFile(config_path=config_path)
        else:
            message = f'Source file not created. Path: {config_path}. Type: {source_type}.'
            raise ValueError(message)

        return source


class Source:
    def __init__(self) -> None:
        # self.source_dict_format = {}
        self.read_only: bool = False
        self.priority: int = 10

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, new_priority):
        if not isinstance(new_priority, int):
            message = "Priority must be int Type."
            raise TypeError(message)
        elif new_priority <= 0:
            message = "Priority can not be negative."
            raise ValueError(message)
        self._priority = new_priority


# inheritance should be in this order because constructor uses super of first class
class SourceFile(Source):
    def __init__(self, input_path: pathlib.Path):
        super().__init__()
        self.path = pathlib.Path(input_path)

    def read_file(self) -> str:
        data: str = self.path.read_text()
        return data

    def save_file(self, data: str):
        if not self.read_only:
            self.path.write_text(data)
        else:
            CONFIGURATOR_LOGGER.info(f'you are trying to write read only config')


class SourceJsonFile(SourceFile, SourceInterface):
    def __init__(self, config_path: pathlib.Path):
        super().__init__(input_path=config_path)
        if self.path.suffix != '.json':
            CONFIGURATOR_LOGGER.warning(f'file extension is not json but format is. file: {self.path}')

    def get_config(self) -> dict:
        data_encoded = self.read_file()
        try:
            data: dict = json.loads(data_encoded)
        except json.JSONDecodeError:
            message = f'Input file is not formatted correctly, JSON expected: "{self.path=}".'
            raise ValueError(message)

        # Check if the loaded data is a dictionary  = Valid_source_data
        if not isinstance(data, dict):
            raise TypeError("JSON file content is not a dictionary.")

        return data

    def save_config(self, data: dict):
        try:
            data_encoded = json.dumps(data, indent=4)
        except TypeError as err:
            CONFIGURATOR_LOGGER.error(f'Error happened: {err}. Probably a data is incorrect. Data for encode to JSON is: {data}')
        else:
            self.save_file(data_encoded)

    def to_dict(self) -> dict:
        attributes_dict = self.__dict__.copy()
        attributes_dict['path'] = str(attributes_dict['path'])
        return attributes_dict


if __name__ == "__main__":
    raise NotImplementedError("this module is not self independent")
