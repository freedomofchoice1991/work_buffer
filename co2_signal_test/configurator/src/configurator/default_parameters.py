import json
import jsonschema
import logging

default_periodical_job_param = {
    "sources": ["main_file", ],
    "enable": True,
    "read_timeout": 100,
    "read_count": 0,
    "write_timeout": 100,
    "write_count": 0
}
periodical_job_schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "sources": {"type": "array"},
        "enable": {"type": "boolean"},
        "read_timeout": {"type": "integer"},
        "read_count": {"type": "integer"},
        "write_timeout": {"type": "integer"},
        "write_count": {"type": "integer"}
    }
}

default_source = {
    "name": "main_file",
    "priority": 1,
    "read_only": True,
    "type": "file_json",
    "link": "config.json",
}
source_schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "name": {"type": "string"},
        "priority": {"type": "integer"},
        "read_only": {"type": "boolean"},
        "type": {"type": "string"},
        "link": {"type": "string"}
    }
}

default_configurator = {
    "name": "global",
    "sources": [default_source, ],
    "periodical_jobs": [default_periodical_job_param, ],
    "version": 1,
    "data": {},
    "data_schema": {}
}
configurator_schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "configurator_name": {"type": "string"},
        "sources": {"type": "array"},
        "periodical_jobs": {"type": "array"},
        "version": {"type": "integer"},
        "data": {"type": "object"},
        "data_schema": {"type": "object"}
    }
}


if __name__ == "__main__":
    print("this module is not self independent")
    print(json.dumps(default_configurator, indent=4))
    try:
        jsonschema.validate(instance=default_periodical_job_param, schema=periodical_job_schema)
        jsonschema.validate(instance=default_source, schema=source_schema)
        jsonschema.validate(instance=default_configurator, schema=configurator_schema)
    except Exception as ex:
        # print(ex)
        logging.error(ex)
