import copy
import logging
from typing import Any, Optional

CONFIGURATOR_LOGGER: logging.Logger


class Config:
    """
    Encapsulates application configuration parameters.

    @arg _no_value: A unique marker used to differentiate no value set from None.
    @arg _data: A dictionary storing the configuration parameters.
    @arg _default: Default value for configuration parameters.
    @arg has_default: Flag indicating whether a default value is set.
    """
    _no_value = object()

    def __init__(self,
                 init_dict: Optional[dict] = None,
                 default: Optional[Any] = _no_value,
                 create_if_not_exists: bool = False):
        """
        Constructor creates a config object

        @param init_dict: Dictionary with initial configuration parameters.
        @param default: Default value for all configuration parameters.
        @param create_if_not_exists: If True, create a parameter with the default value if it does not exist.
        """
        self.has_default = False

        if init_dict is None:
            self._data = {}
        else:
            self._data = init_dict

        self.default = default
        self.create_if_not_exists = create_if_not_exists

    @property
    def default(self) -> Any:
        return self._default

    @default.setter
    def default(self, default_value: Any) -> None:
        if default_value is not self._no_value:
            self._default = default_value
            # Determine if a default value is available for the configuration
            self.has_default = True
        else:
            # This part is not necessary, but may be useful in future if functional for reset default value.
            self.has_default = False

    def is_parameter_exists(self, parameter_name: str) -> bool:
        """@return: True if the parameter exists, False otherwise."""
        exists = parameter_name in self._data
        return exists

    def get_parameter(self, parameter_name: str, **kwargs) -> Any:
        """
        Get parameter value

        @param parameter_name: String Parameter name which is key in dict.
        @param default: Any Value that overwrites default if default allowed
        @return: The parameter's value or a default value if the parameter doesn't exist.
        """
        if self.is_parameter_exists(parameter_name):
            parameter = copy.deepcopy(self._data[parameter_name])
        else:
            if 'default' in kwargs:
                parameter = kwargs['default']
            elif self.has_default:
                parameter = self.default
            else:
                message = f'parameter {parameter_name=} not exists in config and default not set'
                raise ValueError(message)
            if self.create_if_not_exists:
                self.add_parameter(parameter_name=parameter_name, value=parameter)
        return parameter

    def update_parameter(self, parameter_name: str, value: Any) -> None:
        is_parameter_exists = self.is_parameter_exists(parameter_name=parameter_name)
        if not is_parameter_exists:
            raise ValueError('parameter not exists in config')
        else:
            self._data[parameter_name] = copy.deepcopy(value)

    def add_parameter(self, parameter_name: str, value: Any, force: bool = True) -> None:
        if parameter_name in self._data:
            if not force:
                message = f'{parameter_name=} already exists and you do not want to override it({force=}).'
                raise ValueError(message)
            message = f'{parameter_name=} already exists and override.'
            CONFIGURATOR_LOGGER.info(message)
        self._data[parameter_name] = copy.deepcopy(value)

    def delete_parameter(self, parameter_name: str):
        self._data.pop(parameter_name)

    def load_config(self, config: dict):
        self._data = config


if __name__ == "__main__":
    raise NotImplementedError("this module is not self independent")
