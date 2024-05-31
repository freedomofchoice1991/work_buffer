# Configurator

Module to save/load configurations for the project.
The main goal for this module relative to others presented is to create
a possibility for config update from time to time which should be implemented with "periodical job" part (in progress).
Also, it should provide a uniform way how to work with different configuration files like xml, json, yaml and so on.
And the last task is to work with a remote source for the config.

Example 1, create config from prepared file:

To use it, user should create a config file. Minimum config file is:
```json:table
{
    "data": {},
    "name": "test",
    "sources": {},
    "periodical_jobs": {}
}
```
* data - here will be stored all user data
* name - name of the config which should be uniq
* sources - description of all sources for this config (module internal info)
*  periodical_jobs - description of all jobs which should be done for this config (module internal info)

Then configurator should be created with:

my_config = configurator.Configurator.from_file(file_name=config_file_name)

Example 2, create config in memory without an external source and add external file as a source to it:

```python
# create configurator
import configurator

config_name = 'test'
config_file_name = 'my_config.json'

my_config = configurator.Configurator(config_name)
# create a source with source fabric
config_source = my_config.source_fabric(source_type='JSON', file_name=config_file_name)
# add source to configurator
my_config.add_source(input_source=config_source)
# save
my_config.save_configurator()
```

Example 3, singleton usage.

Each configurator has uniq name. If you need parameters in the program, you can call configurator with his uniq name.
```python
# to call configurator from Example 2 in another place
import configurator

config_name = 'test'
my_config_another_place = configurator.Configurator(config_name)
print(my_config_another_place == my_config) 
```
