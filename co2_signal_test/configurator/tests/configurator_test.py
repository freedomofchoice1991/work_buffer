import pytest
import pathlib
import shutil
import random

import configurator


class TestConfigurator:

    def test_configurator_without_name_create(self):
        config_name = ''
        with pytest.raises(ValueError):
            configurator.Configurator(name=config_name)

        config_name = None
        with pytest.raises(ValueError):
            configurator.Configurator(name=config_name)
        pass

    def test_failed_and_successful_create(self):
        config_name = ''
        with pytest.raises(ValueError):
            configurator.Configurator(name=config_name)

        config_name = 'new_configurator'
        new_config = configurator.Configurator(name=config_name)
        assert new_config.name == config_name

    def test_configurator_create(self):
        config_name = 'new_configurator'
        new_config = configurator.Configurator(name=config_name)
        assert new_config.name == config_name

    def test_same_configurator_create(self, configurators_creation):
        [new_config, new_config_same, new_config1, new_config1_same] = configurators_creation
        assert new_config_same == new_config

        test_param_name = 'test param'
        test_param_value = 10
        test_param1_name = 'test param1'
        test_param1_value = 10

        new_config.add_parameter(test_param_name, test_param_value)
        assert new_config_same == new_config
        assert new_config_same.get_parameter(test_param_name) == test_param_value
        new_config_same.add_parameter(test_param1_name, test_param1_value)
        assert new_config_same == new_config
        assert new_config.get_parameter(test_param1_name) == test_param1_value

        assert new_config.is_parameter_exists(test_param1_name)
        assert new_config_same.is_parameter_exists(test_param_name)

        new_config_same.update_parameter(test_param1_name, test_param_value)
        assert new_config_same.get_parameter(test_param1_name) == new_config.get_parameter(test_param_name)

    def test_different_configurator_create(self, configurators_creation):
        [new_config, new_config_same, new_config1, new_config1_same] = configurators_creation
        assert new_config1 != new_config

        test_param_name = 'test param'
        test_param_value = 10

        assert not new_config.is_parameter_exists(test_param_name)
        assert not new_config1.is_parameter_exists(test_param_name)
        new_config.add_parameter(test_param_name, test_param_value)
        assert new_config1 != new_config
        assert new_config.is_parameter_exists(test_param_name)
        assert not new_config1.is_parameter_exists(test_param_name)
        with pytest.raises(ValueError):
            new_config1.get_parameter(test_param_name)

    @pytest.fixture(scope='function')
    def configurators_creation(self):
        config_name = 'new_configurator'
        config_name1 = 'new_configurator1'
        new_config = configurator.Configurator(name=config_name)
        new_config_same = configurator.Configurator(name=config_name)
        new_config1 = configurator.Configurator(name=config_name1)
        new_config1_same = configurator.Configurator(name=config_name1)
        configurators = [new_config, new_config_same, new_config1, new_config1_same]

        yield configurators

        for configurator_ in configurators:
            if configurator_.is_configurator_exists():
                configurator_.remove_configurator()
        pass

    def test_add_param(self, configurators_creation):
        example_config1 = configurators_creation[0]

        param_name = 'number_of_customers'
        param_value = random.random()

        example_config1.add_parameter(parameter_name=param_name, value=param_value)
        number_of_customers = example_config1.get_parameter(param_name)

        assert param_value == number_of_customers

    def test_update_param(self, configurators_creation):
        example_config1 = configurators_creation[0]
        example_config2 = configurators_creation[1]

        param_name = 'number_of_customers'
        param_value = random.random()

        example_config1.add_parameter(parameter_name=param_name, value=param_value)
        number_of_customers = example_config2.get_parameter(param_name)

        assert param_value == number_of_customers

    def test_update_non_existing_parameter(self, configurators_creation):
        example_config = configurators_creation[0]
        with pytest.raises(ValueError):
            example_config.update_parameter('non_existing_parameter', 'updated_value')

    def test_delete_param(self, configurators_creation):
        example_config1 = configurators_creation[0]

        param_name1 = 'number_of_customers'
        param_name2 = 'money'
        non_exist_param = 'tax_class'
        param_value = random.random()
        example_config1.add_parameter(parameter_name=param_name1, value=param_value)
        example_config1.add_parameter(parameter_name=param_name2, value=param_value)

        example_config1.delete_parameter(parameter_name=param_name1)

        assert not example_config1.is_parameter_exists(parameter_name=param_name1)

        assert example_config1.is_parameter_exists(parameter_name=param_name2)

        with pytest.raises(KeyError):
            example_config1.delete_parameter(parameter_name=non_exist_param)

    def test_change_name_json(self, configurators_creation):
        example_config1 = configurators_creation[0]
        old_name = example_config1.name
        new_name = old_name + 'new_name'
        example_config1.name = new_name
        assert example_config1.name == new_name
        assert example_config1.name != old_name

    @pytest.fixture
    def json_source_create(self, tmp_path):
        TEMPLATE_CONFIG_FILE = 'test-conf.json'
        TEMPLATE_CONFIG_FILE1 = 'test-conf1.json'
        TEMPLATE_SUBDIR = 'resources'

        path_to_example = pathlib.Path(pathlib.Path.cwd()) / TEMPLATE_SUBDIR / TEMPLATE_CONFIG_FILE
        tmp_config_path = pathlib.Path(tmp_path) / TEMPLATE_CONFIG_FILE
        tmp_config1_path = pathlib.Path(tmp_path) / TEMPLATE_CONFIG_FILE1
        shutil.copy(path_to_example, tmp_config_path)
        shutil.copy(path_to_example, tmp_config1_path)

        return [tmp_config_path, tmp_config1_path]

    # TODO rewrite this tests
    # @pytest.fixture
    # def add_source_creation(self):
    #     config_name = 'test config'
    #     config_file_name = 'test.json'
    #
    #     my_config = configurator.Configurator(config_name)
    #     config_source = my_config.source_fabric(source_type='JSON', file_name=config_file_name)
    #
    #     return [my_config, config_source]
    #
    # def test_add_source(self, add_source_creation):
    #     my_config = add_source_creation[0]
    #     config_source = add_source_creation[1]
    #
    #     assert len(my_config.get_sources()) == 0
    #     my_config.add_source(input_source=config_source)
    #     assert len(my_config.get_sources()) == 1
    #
    # def test_delete_source(self, add_source_creation):
    #     my_config = add_source_creation[0]
    #     config_source = add_source_creation[1]
    #
    #     my_config.add_source(input_source=config_source)
    #     sources_keys = my_config.get_sources().keys()
    #     for key in list(sources_keys):
    #         my_config.delete_source(key)
    #     assert len(my_config.get_sources()) == 0
    #
    # def test_delete_non_existing_source(self, add_source_creation):
    #     my_config = add_source_creation[0]
    #
    #     with pytest.raises(ValueError):
    #         my_config.delete_source(source_id=-10)
    #
    # def test_check_source(self, add_source_creation):
    #     my_config = add_source_creation[0]
    #     config_source = add_source_creation[1]
    #
    #     my_config.add_source(input_source=config_source)
    #     sources_keys = my_config.get_sources().keys()
    #     for key in sources_keys:
    #         assert my_config.is_source_exist(key)

    def test_load_two_json(self, json_source_create):
        source_path2 = json_source_create[0]
        example_config1 = configurator.Configurator.from_file(file_path=str(source_path2))
        name1_old = example_config1.name
        name1_new = name1_old + '1'
        example_config1.name = name1_new
        example_config1.save_configurator()

        # check that name changed
        assert example_config1.name == name1_new
        assert example_config1.name != name1_old

        source_path2 = json_source_create[1]
        example_config2 = configurator.Configurator.from_file(file_path=str(source_path2))

        # names should be different
        assert example_config1.name != example_config2.name

    def test_save_load_param_json(self, json_source_create):
        source_path = json_source_create[0]
        example_config1 = configurator.Configurator.from_file(file_path=str(source_path))

        param_name = 'number_of_customers'
        param_value = random.random()

        example_config1.add_parameter(parameter_name=param_name, value=param_value)
        example_config1.save_configurator()
        example_config1.update_configurator()
        number_of_customers = example_config1.get_parameter(param_name)

        assert param_value == number_of_customers

    def test_change_name_json(self, json_source_create):
        source_path0 = json_source_create[0]

        example_config1 = configurator.Configurator.from_file(file_path=str(source_path0))
        old_name = example_config1.name
        new_name = old_name + 'new_name'
        example_config1.name = new_name
        example_config1.save_configurator()
        example_config1.update_configurator()
        assert example_config1.name == new_name
        assert example_config1.name != old_name

    def test_same_configurator_from_json(self, json_source_create):
        source_path = json_source_create[0]
        example_config1 = configurator.Configurator.from_file(file_path=str(source_path))
        example_config2 = configurator.Configurator.from_file(file_path=str(source_path))
        assert example_config1 == example_config2

    def test_save_load_json(self, json_source_create):
        source_path0 = json_source_create[0]
        source_path1 = json_source_create[1]

        example_config1 = configurator.Configurator.from_file(file_path=str(source_path0))
        example_config1.name = 'new_name'
        example_config2 = configurator.Configurator.from_file(file_path=str(source_path1))

        param_name = 'number_of_customers'
        param_value = random.random()

        example_config1.add_parameter(parameter_name=param_name, value=param_value)
        example_config1.save_configurator()

        number_of_customers = example_config1.get_parameter(param_name)

        assert example_config2 is not example_config1

        new_value = param_value + 1

        example_config2.update_parameter(param_name, new_value)

        number_of_customers_conf1 = example_config1.get_parameter(param_name)
        number_of_customers_conf2 = example_config2.get_parameter(param_name)

        assert number_of_customers_conf1 != number_of_customers_conf2
