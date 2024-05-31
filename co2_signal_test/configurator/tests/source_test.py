import pytest
import source
import json
import pathlib
import shutil


class TestSource:

    @pytest.fixture
    def source_creation(self, tmp_path):
        TEMPLATE_SOURCE_FILE = 'test-conf.json'
        TEMPLATE_SUBDIR = 'resources'

        path_to_example = pathlib.Path(pathlib.Path.cwd()) / TEMPLATE_SUBDIR / TEMPLATE_SOURCE_FILE
        path_tmp_source = pathlib.Path(tmp_path) / TEMPLATE_SOURCE_FILE
        shutil.copy(path_to_example, path_tmp_source)

        return str(path_tmp_source)

    def test_source_priority(self, source_creation):
        source_path = source_creation
        example_source = source.SourceFabric.create_source(path=source_path)
        with pytest.raises(TypeError):
            example_source.priority = 4.7

        with pytest.raises(ValueError):
            example_source.priority = -5

        example_source.priority = 99
        assert isinstance(example_source.priority, int)
        assert example_source.priority == 99

    def test_creating_json_source_with_invalid_source_type(self, tmp_path):
        file_name = 'test.xml'
        source_type = 'xml'
        path = str(tmp_path)
        with pytest.raises(ValueError):
            source.SourceFabric.create_source(file_name=file_name, source_type=source_type, path=path)

    def test_to_dict(self, source_creation):
        source_path = source_creation
        example_source = source.SourceFabric.create_source(path=source_path)
        expected_dict = {'read_only': False, '_priority': 10, 'path': source_path}
        assert example_source.to_dict() == expected_dict

    def test_get_config_from_valid_json_source(self, source_creation):
        source_path = source_creation
        example_source = source.SourceFabric.create_source(path=source_path)
        valid_json_data = {
            "data": {
                "number_of_customers": 17
            },
            "name": "test_get_config",
            "version": 1.05,
            "sources": {},
            "periodical_jobs": {}
        }

        with open(source_path, 'w') as file:
            json.dump(valid_json_data, file, indent=4)
        assert example_source.get_config() == valid_json_data

    def test_get_config_from_invalid_json_source(self, source_creation):
        source_path = source_creation
        example_source = source.SourceFabric.create_source(path=source_path)
        invalid_json_data = "This is just a simple string."

        with open(source_path, 'w') as file:
            json.dump(invalid_json_data, file)

        with pytest.raises(TypeError):
            example_source.get_config()

    def test_source_fabric_constructor(self):
        with pytest.raises(NotImplementedError):
            source.SourceFabric()

        with pytest.raises(ValueError):
            source.SourceFabric.create_source()

        with pytest.raises(NotImplementedError):
            source.SourceFabric.create_source(url='')

        with pytest.raises(NotImplementedError):
            source.SourceFabric.create_source(variable='')

    def test_source_file_constructor(self, tmp_path):
        file_name = 'test.json'
        subdir = 'configs'
        path = str(tmp_path / file_name)

        new_source = source.SourceFabric.create_source(path=path)
        assert isinstance(new_source, source.Source)

        path = str(tmp_path / subdir / file_name)
        new_source = source.SourceFabric.create_source(path=path)
        assert isinstance(new_source, source.Source)

        path = str(tmp_path)
        new_source = source.SourceFabric.create_source(path=path, file_name=file_name, subdir=subdir)
        assert isinstance(new_source, source.Source)

        path = str(tmp_path)
        new_source = source.SourceFabric.create_source(path=path, file_name=file_name)
        assert isinstance(new_source, source.Source)

        with pytest.raises(ValueError):
            new_source = source.SourceFabric.create_source(path=1)

        with pytest.raises(ValueError):
            new_source = source.SourceFabric.create_source(path=path, source_type=1)

        path = str(tmp_path / subdir / file_name) + '1'
        with pytest.raises(ValueError):
            new_source = source.SourceFabric.create_source(path=path)
