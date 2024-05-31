import logging
from typing import Optional, TYPE_CHECKING, Iterable

from .singleton import Singleton

# this part is for avoid cross import but keep type check. better solution is not found.
if TYPE_CHECKING:
    from .configurator import Configurator

CONFIGURATOR_LOGGER: logging.Logger


class Referee(Singleton):
    @Singleton._init_deco
    def __init__(self):
        self.__configurators = {}

    def add_configurator(self, input_configurator: 'Configurator'):
        self.__configurators[input_configurator.name] = input_configurator

    def is_configurator_exists(self, configurator_name: Optional[str] = None) -> bool:
        configurator_exists = False

        if configurator_name in self.__configurators:
            configurator_exists = True

        return configurator_exists

    def get_configurator(self, configurator_name: str) -> 'Configurator':
        configurator = self.__configurators.get(configurator_name)
        return configurator

    def merge(self, configurator_source: 'Configurator', configurator_target: 'Configurator'):
        # TODO not implemented
        self.__configurators[configurator_target.name] = configurator_source

    def show_all_configurators(self) -> Iterable[str]:
        return self.__configurators.keys()

    def name_changed(self, configurator: 'Configurator'):
        if not self.is_configurator_exists(configurator_name=configurator.name):
            # add configurator new name
            self.add_configurator(configurator)
        else:
            # new name is busy
            target_configurator = self.get_configurator(configurator.name)
            self.merge(configurator, target_configurator)
            message = f'New configurator name is busy {configurator.name=} merged.'
            CONFIGURATOR_LOGGER.debug(message)
        # remove old record(s) for configurator but do not touch new record
        configurator_old_names = []
        for configurator_name, value in self.__configurators.items():
            if (value is configurator) and (configurator_name != configurator.name):
                configurator_old_names.append(configurator_name)
                # this part should never happen, warn about it
                if len(configurator_old_names) > 1:
                    message = f'more than one record for a configurator {configurator_name=} list is {configurator_old_names=}'
                    CONFIGURATOR_LOGGER.warning(message)
                elif len(configurator_old_names) < 1:
                    message = f'less than one record for a configurator {configurator_name=} list is {configurator_old_names=}'
                    CONFIGURATOR_LOGGER.warning(message)
        for configurator_name in configurator_old_names:
            self.remove_configurator(configurator_name)
        pass

    def remove_configurator(self, configurator_name: str):
        del self.__configurators[configurator_name]


if __name__ == "__main__":
    raise NotImplementedError("this module is not self independent")
