Alternative Services to electricitymaps.com

There are a few services I have found:
---------------------------------------------
# Eurostat website
Datasets are updated twice a day

[https://ec.europa.eu/eurostat/web/main/home]
# API
[https://ec.europa.eu/eurostat/web/main/data/web-services]

---------------------------------------------
# Ember climate org website
Could not found API in it but it has DATA-TOOLS and datasets
[https://ember-climate.org/data/data-tools/]
[https://ember-climate.org/data/data-tools/data-explorer/]
[https://ember-climate.org/data/data-catalogue/]

Datasets I found related to electricity were yearly and monthly not daily:

Dataset: (Monthly electricity Data 2018 - 2023)

Dataset: (Yearly electricity Data 2000 - 2023)

---------------------------------------------
# Energy-chart info website

This website has charts much detailed than electricitymaps service and it could be customized:

[https://www.energy-charts.info/charts/energy/chart.htm?l=en&c=DE]

This website has also an API:
[https://api.energy-charts.info/]

---------------------------------------------
# Open power system Data website

[https://open-power-system-data.org/]

This website has packages of data and in order to use them I could not find API documentation but there is an step by step guide:

[https://open-power-system-data.org/step-by-step]


---------------------------------------------
# Energy Institute website

In this one we could make a chart by customization
Worth looking

[https://www.energyinst.org/statistical-review/energy-charting-tool/energy-charting-tool]

This website was used to create charts for wikipedia of electricity energy page of Germany
This website has Datasets for download but could not find API

---------------------------------------------
# SMARD  website                   Electricity generation and consumption in Germany

[https://www.smard.de/en]

This website has a download section which I believe is the closeset to what you described. Because it can be customized based on date, resolution, ....

[https://www.smard.de/en/downloadcenter/download-market-data/]

---------------------------------------------
# US Energy information Administration

The EIA publishes weekly, monthly and annual reports on various energy carriers and their usage around the world. All data is available free of charge and can be downloaded in machine-readable formats (CSV, XLS, JSON) or retrieved directly via the API.

Germany overview and datasets : [https://www.eia.gov/international/data/country/DEU]


API: [https://www.eia.gov/developer/]

---------------------------------------------
# STATISTA    website

[https://www.eia.gov/international/data/country/DEU]

[https://www.statista.com/statistics/383650/consumption-of-electricity-in-germany/]

---------------------------------------------
# International Renewable Energy Agency website

The international renewable energy agency publishes reports as well as data on the generation and use of renewable energy. Data can be visualized directly in the web app and downloaded as PDF, PPTX or CSV for free.

[https://www.irena.org/Data]

[https://pxweb.irena.org/pxweb/en/IRENASTAT/IRENASTAT__Power%20Capacity%20and%20Generation/REGEN_2023_cycle2.px/]

---------------------------------------------
# International Energy Agency website

The international energy agency publishes loads of historic energy data as well as forecasts by energy source. Reports can be downloaded for free and charts are available in the web interface.

[https://www.iea.org/data-and-statistics]

[https://www.iea.org/data-and-statistics/data-tools/monthly-electricity-statistics]
---------------------------------------------



---------------------------------------------
There are a few more websites which I was not sure if they are as good as aforementioned websites but still giving link does not hurt:

[https://www.agora-energiewende.org/data-tools/agorameter/chart/today/power_generation/15.01.2024/14.02.2024/daily]


[https://www.carbonbrief.org/how-germany-generates-its-electricity/]


# DATA we receive from API:
---------------------------------------------
Carbon intensity  - latest:

{'zone': 'DE', 'carbonIntensity': 371, 'datetime': '2024-02-21T08:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T08:49:11.590Z', 'emissionFactorType': 'lifecycle', 'isEstimated': True, 'estimationMethod': 'TIME_SLICER_AVERAGE'}

zone: DE
carbonIntensity: 371
datetime: 2024-02-21T08:00:00.000Z
updatedAt: 2024-02-21T07:47:25.183Z
createdAt: 2024-02-18T08:49:11.590Z
emissionFactorType: lifecycle
isEstimated: True
estimationMethod: TIME_SLICER_AVERAGE
---------------------------------------------
Carbon intensity  - history:

{'zone': 'DE', 'history': [{'zone': 'DE', 'carbonIntensity': 365, 'datetime': '2024-02-20T09:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T09:47:08.464Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 326, 'datetime': '2024-02-20T10:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T10:50:53.281Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 289, 'datetime': '2024-02-20T11:00:00.000Z', 'updatedAt': '2024-02-21T07:47:04.377Z', 'createdAt': '2024-02-17T11:48:16.694Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 283, 'datetime': '2024-02-20T12:00:00.000Z', 'updatedAt': '2024-02-21T07:47:19.932Z', 'createdAt': '2024-02-17T12:46:55.300Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 293, 'datetime': '2024-02-20T13:00:00.000Z', 'updatedAt': '2024-02-21T07:47:04.377Z', 'createdAt': '2024-02-17T13:50:52.925Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 326, 'datetime': '2024-02-20T14:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T14:44:09.743Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 363, 'datetime': '2024-02-20T15:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T15:47:56.985Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 390, 'datetime': '2024-02-20T16:00:00.000Z', 'updatedAt': '2024-02-21T07:47:04.377Z', 'createdAt': '2024-02-17T16:45:46.574Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 396, 'datetime': '2024-02-20T17:00:00.000Z', 'updatedAt': '2024-02-21T07:47:04.377Z', 'createdAt': '2024-02-17T17:48:28.195Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 397, 'datetime': '2024-02-20T18:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T18:46:41.049Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 369, 'datetime': '2024-02-20T19:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T19:49:40.189Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 350, 'datetime': '2024-02-20T20:00:00.000Z', 'updatedAt': '2024-02-21T01:49:42.818Z', 'createdAt': '2024-02-17T20:48:21.810Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 343, 'datetime': '2024-02-20T21:00:00.000Z', 'updatedAt': '2024-02-21T06:50:16.054Z', 'createdAt': '2024-02-17T21:47:11.494Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 336, 'datetime': '2024-02-20T22:00:00.000Z', 'updatedAt': '2024-02-21T06:50:35.325Z', 'createdAt': '2024-02-17T22:49:08.295Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 300, 'datetime': '2024-02-20T23:00:00.000Z', 'updatedAt': '2024-02-21T06:50:16.054Z', 'createdAt': '2024-02-17T23:49:07.838Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 282, 'datetime': '2024-02-21T00:00:00.000Z', 'updatedAt': '2024-02-21T06:50:07.873Z', 'createdAt': '2024-02-18T00:51:36.182Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 285, 'datetime': '2024-02-21T01:00:00.000Z', 'updatedAt': '2024-02-21T06:50:07.873Z', 'createdAt': '2024-02-18T01:48:12.169Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 291, 'datetime': '2024-02-21T02:00:00.000Z', 'updatedAt': '2024-02-21T06:50:35.325Z', 'createdAt': '2024-02-18T02:56:30.383Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 295, 'datetime': '2024-02-21T03:00:00.000Z', 'updatedAt': '2024-02-21T06:49:44.221Z', 'createdAt': '2024-02-18T03:46:41.338Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 328, 'datetime': '2024-02-21T04:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T04:49:46.463Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 349, 'datetime': '2024-02-21T05:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T05:47:41.840Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 355, 'datetime': '2024-02-21T06:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T06:45:17.837Z', 'emissionFactorType': 'lifecycle', 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'carbonIntensity': 376, 'datetime': '2024-02-21T07:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T07:47:28.867Z', 'emissionFactorType': 'lifecycle', 'isEstimated': True, 'estimationMethod': 'TIME_SLICER_AVERAGE'}, {'zone': 'DE', 'carbonIntensity': 371, 'datetime': '2024-02-21T08:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T08:49:11.590Z', 'emissionFactorType': 'lifecycle', 'isEstimated': True, 'estimationMethod': 'TIME_SLICER_AVERAGE'}]}

zone: DE
carbonIntensity: 365
datetime: 2024-02-20T09:00:00.000Z
updatedAt: 2024-02-21T07:47:25.183Z
createdAt: 2024-02-17T09:47:08.464Z
emissionFactorType: lifecycle
isEstimated: False
estimationMethod: None



zone: DE
carbonIntensity: 326
datetime: 2024-02-20T10:00:00.000Z
updatedAt: 2024-02-21T07:47:25.183Z
createdAt: 2024-02-17T10:50:53.281Z
emissionFactorType: lifecycle
isEstimated: False
estimationMethod: None



zone: DE
carbonIntensity: 289
datetime: 2024-02-20T11:00:00.000Z
updatedAt: 2024-02-21T07:47:04.377Z
createdAt: 2024-02-17T11:48:16.694Z
emissionFactorType: lifecycle
isEstimated: False
estimationMethod: None



zone: DE
carbonIntensity: 283
datetime: 2024-02-20T12:00:00.000Z
updatedAt: 2024-02-21T07:47:19.932Z
createdAt: 2024-02-17T12:46:55.300Z
emissionFactorType: lifecycle
isEstimated: False
estimationMethod: None



zone: DE
carbonIntensity: 293
datetime: 2024-02-20T13:00:00.000Z
updatedAt: 2024-02-21T07:47:04.377Z
createdAt: 2024-02-17T13:50:52.925Z
emissionFactorType: lifecycle
isEstimated: False
estimationMethod: None

.....
.....
.....


---------------------------------------------
power breakdown - latest:

{'zone': 'DE', 'datetime': '2024-02-21T08:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T08:49:11.590Z', 'powerConsumptionBreakdown': {'nuclear': 260, 'geothermal': 22, 'biomass': 5540, 'coal': 12757, 'wind': 25861, 'solar': 3308, 'hydro': 2103, 'gas': 7161, 'oil': 332, 'unknown': 236, 'hydro discharge': 2523, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5466, 'coal': 12929, 'wind': 25507, 'solar': 3319, 'hydro': 1906, 'gas': 7168, 'oil': 325, 'unknown': 197, 'hydro discharge': 2522, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 714, 'CH': 1094, 'CZ': 0, 'LU': 0, 'NL': 1496, 'DK-DK1': 181, 'DK-DK2': 646, 'NO-NO2': 602}, 'powerExportBreakdown': {'AT': 1328, 'BE': 0, 'CH': 0, 'CZ': 2210, 'LU': 455, 'NL': 0, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0}, 'fossilFreePercentage': 66, 'renewablePercentage': 65, 'powerConsumptionTotal': 60101, 'powerProductionTotal': 59360, 'powerImportTotal': 4734, 'powerExportTotal': 3993, 'isEstimated': True, 'estimationMethod': 'TIME_SLICER_AVERAGE'}


zone: DE
datetime: 2024-02-21T08:00:00.000Z
updatedAt: 2024-02-21T07:47:25.183Z
createdAt: 2024-02-18T08:49:11.590Z
powerConsumptionBreakdown: {'nuclear': 260, 'geothermal': 22, 'biomass': 5540, 'coal': 12757, 'wind': 25861, 'solar': 3308, 'hydro': 2103, 'gas': 7161, 'oil': 332, 'unknown': 236, 'hydro discharge': 2523, 'battery discharge': 0}
powerProductionBreakdown: {'nuclear': None, 'geothermal': 22, 'biomass': 5466, 'coal': 12929, 'wind': 25507, 'solar': 3319, 'hydro': 1906, 'gas': 7168, 'oil': 325, 'unknown': 197, 'hydro discharge': 2522, 'battery discharge': None}
powerImportBreakdown: {'AT': 0, 'BE': 714, 'CH': 1094, 'CZ': 0, 'LU': 0, 'NL': 1496, 'DK-DK1': 181, 'DK-DK2': 646, 'NO-NO2': 602}
powerExportBreakdown: {'AT': 1328, 'BE': 0, 'CH': 0, 'CZ': 2210, 'LU': 455, 'NL': 0, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0}
fossilFreePercentage: 66
renewablePercentage: 65
powerConsumptionTotal: 60101
powerProductionTotal: 59360
powerImportTotal: 4734
powerExportTotal: 3993
isEstimated: True
estimationMethod: TIME_SLICER_AVERAGE

---------------------------------------------
power breakdown - history:

{'zone': 'DE', 'history': [{'zone': 'DE', 'datetime': '2024-02-20T09:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T09:47:08.464Z', 'powerConsumptionBreakdown': {'nuclear': 2432, 'geothermal': 20, 'biomass': 5228, 'coal': 13581, 'wind': 17178, 'solar': 11807, 'hydro': 3289, 'gas': 7576, 'oil': 335, 'unknown': 298, 'hydro discharge': 1656, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5391, 'coal': 14718, 'wind': 17813, 'solar': 11883, 'hydro': 2003, 'gas': 7718, 'oil': 329, 'unknown': 192, 'hydro discharge': 1510, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 1422, 'CZ': 0, 'FR': 3509, 'LU': 0, 'NL': 1793, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 606, 'NO-NO2': 651}, 'powerExportBreakdown': {'AT': 888, 'BE': 473, 'CH': 0, 'CZ': 1881, 'FR': 0, 'LU': 373, 'NL': 0, 'PL': 1675, 'DK-DK1': 868, 'DK-DK2': 0, 'NO-NO2': 0}, 'fossilFreePercentage': 66, 'renewablePercentage': 62, 'powerConsumptionTotal': 63400, 'powerProductionTotal': 61577, 'powerImportTotal': 7980, 'powerExportTotal': 6158, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T10:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T10:50:53.281Z', 'powerConsumptionBreakdown': {'nuclear': 1820, 'geothermal': 20, 'biomass': 5138, 'coal': 12106, 'wind': 19339, 'solar': 14395, 'hydro': 2889, 'gas': 7277, 'oil': 331, 'unknown': 238, 'hydro discharge': 464, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5443, 'coal': 13153, 'wind': 19842, 'solar': 14617, 'hydro': 1929, 'gas': 7511, 'oil': 330, 'unknown': 192, 'hydro discharge': 285, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 181, 'CZ': 0, 'FR': 2765, 'LU': 0, 'NL': 2454, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 749, 'NO-NO2': 685, 'SE-SE4': 292}, 'powerExportBreakdown': {'AT': 1509, 'BE': 798, 'CH': 0, 'CZ': 1519, 'FR': 0, 'LU': 430, 'NL': 0, 'PL': 1596, 'DK-DK1': 579, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 69, 'renewablePercentage': 66, 'powerConsumptionTotal': 64017, 'powerProductionTotal': 63323, 'powerImportTotal': 7125, 'powerExportTotal': 6431, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T11:00:00.000Z', 'updatedAt': '2024-02-21T07:47:04.377Z', 'createdAt': '2024-02-17T11:48:16.694Z', 'powerConsumptionBreakdown': {'nuclear': 1469, 'geothermal': 20, 'biomass': 5134, 'coal': 10522, 'wind': 21857, 'solar': 15049, 'hydro': 2728, 'gas': 6554, 'oil': 322, 'unknown': 209, 'hydro discharge': 52, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5537, 'coal': 11613, 'wind': 22804, 'solar': 15405, 'hydro': 1971, 'gas': 6901, 'oil': 330, 'unknown': 192, 'hydro discharge': -1667, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 2, 'CH': 144, 'CZ': 0, 'FR': 2331, 'LU': 0, 'NL': 2771, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 734, 'NO-NO2': 687, 'SE-SE4': 30}, 'powerExportBreakdown': {'AT': 1598, 'BE': 0, 'CH': 0, 'CZ': 1879, 'FR': 0, 'LU': 425, 'NL': 0, 'PL': 1646, 'DK-DK1': 341, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 72, 'renewablePercentage': 70, 'powerConsumptionTotal': 63915, 'powerProductionTotal': 64772, 'powerImportTotal': 6699, 'powerExportTotal': 5889, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T12:00:00.000Z', 'updatedAt': '2024-02-21T07:47:19.932Z', 'createdAt': '2024-02-17T12:46:55.300Z', 'powerConsumptionBreakdown': {'nuclear': 1836, 'geothermal': 19, 'biomass': 5024, 'coal': 10174, 'wind': 22899, 'solar': 13730, 'hydro': 2728, 'gas': 6345, 'oil': 315, 'unknown': 195, 'hydro discharge': 36, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5575, 'coal': 11470, 'wind': 24338, 'solar': 14013, 'hydro': 2036, 'gas': 6786, 'oil': 330, 'unknown': 192, 'hydro discharge': -1952, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 267, 'CZ': 0, 'FR': 3004, 'LU': 0, 'NL': 3318, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 248, 'NO-NO2': 687}, 'powerExportBreakdown': {'AT': 1676, 'BE': 666, 'CH': 0, 'CZ': 2287, 'FR': 0, 'LU': 357, 'NL': 0, 'PL': 1817, 'DK-DK1': 232, 'DK-DK2': 0, 'NO-NO2': 0}, 'fossilFreePercentage': 73, 'renewablePercentage': 70, 'powerConsumptionTotal': 63299, 'powerProductionTotal': 64760, 'powerImportTotal': 7524, 'powerExportTotal': 7033, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T13:00:00.000Z', 'updatedAt': '2024-02-21T07:47:04.377Z', 'createdAt': '2024-02-17T13:50:52.925Z', 'powerConsumptionBreakdown': {'nuclear': 1854, 'geothermal': 19, 'biomass': 5110, 'coal': 10472, 'wind': 23509, 'solar': 11345, 'hydro': 2801, 'gas': 6257, 'oil': 321, 'unknown': 187, 'hydro discharge': 30, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5599, 'coal': 11749, 'wind': 24886, 'solar': 11469, 'hydro': 2167, 'gas': 6691, 'oil': 330, 'unknown': 192, 'hydro discharge': -1703, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 15, 'CZ': 0, 'FR': 3082, 'LU': 0, 'NL': 2855, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 683, 'NO-NO2': 687}, 'powerExportBreakdown': {'AT': 1866, 'BE': 155, 'CH': 0, 'CZ': 2047, 'FR': 0, 'LU': 397, 'NL': 0, 'PL': 1692, 'DK-DK1': 660, 'DK-DK2': 0, 'NO-NO2': 0}, 'fossilFreePercentage': 72, 'renewablePercentage': 69, 'powerConsumptionTotal': 61907, 'powerProductionTotal': 63105, 'powerImportTotal': 7322, 'powerExportTotal': 6817, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T14:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T14:44:09.743Z', 'powerConsumptionBreakdown': {'nuclear': 2240, 'geothermal': 20, 'biomass': 5344, 'coal': 11527, 'wind': 22855, 'solar': 7777, 'hydro': 3064, 'gas': 6720, 'oil': 330, 'unknown': 232, 'hydro discharge': 462, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5639, 'coal': 12536, 'wind': 23560, 'solar': 7465, 'hydro': 2110, 'gas': 7007, 'oil': 330, 'unknown': 192, 'hydro discharge': 255, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 30, 'CH': 351, 'CZ': 0, 'FR': 3252, 'LU': 0, 'NL': 2081, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 719, 'NO-NO2': 687, 'SE-SE4': 161}, 'powerExportBreakdown': {'AT': 1734, 'BE': 0, 'CH': 0, 'CZ': 2096, 'FR': 0, 'LU': 454, 'NL': 0, 'PL': 1461, 'DK-DK1': 79, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 69, 'renewablePercentage': 65, 'powerConsumptionTotal': 60571, 'powerProductionTotal': 59114, 'powerImportTotal': 7280, 'powerExportTotal': 5823, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T15:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T15:47:56.985Z', 'powerConsumptionBreakdown': {'nuclear': 3263, 'geothermal': 20, 'biomass': 5547, 'coal': 12637, 'wind': 21875, 'solar': 3529, 'hydro': 3525, 'gas': 7282, 'oil': 332, 'unknown': 340, 'hydro discharge': 1213, 'battery discharge': 1}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5698, 'coal': 13634, 'wind': 22201, 'solar': 2998, 'hydro': 2059, 'gas': 7490, 'oil': 330, 'unknown': 192, 'hydro discharge': 1157, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 920, 'CH': 1265, 'CZ': 0, 'FR': 3622, 'LU': 0, 'NL': 1329, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 736, 'NO-NO2': 687, 'SE-SE4': 547}, 'powerExportBreakdown': {'AT': 1125, 'BE': 0, 'CH': 0, 'CZ': 1997, 'FR': 0, 'LU': 502, 'NL': 0, 'PL': 1547, 'DK-DK1': 151, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 66, 'renewablePercentage': 60, 'powerConsumptionTotal': 59564, 'powerProductionTotal': 55780, 'powerImportTotal': 9106, 'powerExportTotal': 5322, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T16:00:00.000Z', 'updatedAt': '2024-02-21T07:47:04.377Z', 'createdAt': '2024-02-17T16:45:46.574Z', 'powerConsumptionBreakdown': {'nuclear': 3635, 'geothermal': 20, 'biomass': 5742, 'coal': 13926, 'wind': 22011, 'solar': 630, 'hydro': 4060, 'gas': 7519, 'oil': 332, 'unknown': 414, 'hydro discharge': 3084, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5725, 'coal': 14881, 'wind': 22299, 'solar': 314, 'hydro': 2131, 'gas': 7656, 'oil': 329, 'unknown': 192, 'hydro discharge': 2858, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 918, 'CH': 2212, 'CZ': 0, 'FR': 3872, 'LU': 0, 'NL': 459, 'PL': 0, 'DK-DK1': 178, 'DK-DK2': 761, 'NO-NO2': 687, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 491, 'BE': 0, 'CH': 0, 'CZ': 2108, 'FR': 0, 'LU': 557, 'NL': 0, 'PL': 1578, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 64, 'renewablePercentage': 58, 'powerConsumptionTotal': 61374, 'powerProductionTotal': 56407, 'powerImportTotal': 9703, 'powerExportTotal': 4735, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T17:00:00.000Z', 'updatedAt': '2024-02-21T07:47:04.377Z', 'createdAt': '2024-02-17T17:48:28.195Z', 'powerConsumptionBreakdown': {'nuclear': 2842, 'geothermal': 20, 'biomass': 5673, 'coal': 14787, 'wind': 24191, 'solar': 31, 'hydro': 3986, 'gas': 7712, 'oil': 332, 'unknown': 379, 'hydro discharge': 3714, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5717, 'coal': 15806, 'wind': 24486, 'solar': 0, 'hydro': 2107, 'gas': 7764, 'oil': 329, 'unknown': 192, 'hydro discharge': 3454, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 1897, 'CZ': 0, 'FR': 3546, 'LU': 0, 'NL': 1371, 'PL': 0, 'DK-DK1': 97, 'DK-DK2': 602, 'NO-NO2': 687, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 574, 'BE': 73, 'CH': 0, 'CZ': 2122, 'FR': 0, 'LU': 517, 'NL': 0, 'PL': 1740, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 64, 'renewablePercentage': 59, 'powerConsumptionTotal': 63667, 'powerProductionTotal': 59876, 'powerImportTotal': 8817, 'powerExportTotal': 5026, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T18:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T18:46:41.049Z', 'powerConsumptionBreakdown': {'nuclear': 1794, 'geothermal': 20, 'biomass': 5542, 'coal': 14887, 'wind': 26291, 'solar': 2, 'hydro': 3318, 'gas': 7713, 'oil': 325, 'unknown': 301, 'hydro discharge': 2479, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5684, 'coal': 15902, 'wind': 27123, 'solar': 0, 'hydro': 1944, 'gas': 7998, 'oil': 329, 'unknown': 192, 'hydro discharge': 2370, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 18, 'CH': 804, 'CZ': 0, 'FR': 2235, 'LU': 0, 'NL': 536, 'PL': 0, 'DK-DK1': 73, 'DK-DK2': 761, 'NO-NO2': 687, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 685, 'BE': 0, 'CH': 0, 'CZ': 1760, 'FR': 0, 'LU': 575, 'NL': 0, 'PL': 1601, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 63, 'renewablePercentage': 60, 'powerConsumptionTotal': 62674, 'powerProductionTotal': 61564, 'powerImportTotal': 5731, 'powerExportTotal': 4621, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T19:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-17T19:49:40.189Z', 'powerConsumptionBreakdown': {'nuclear': 1297, 'geothermal': 20, 'biomass': 5331, 'coal': 13198, 'wind': 28038, 'solar': 0, 'hydro': 3004, 'gas': 7374, 'oil': 316, 'unknown': 249, 'hydro discharge': 481, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5627, 'coal': 14333, 'wind': 29592, 'solar': 0, 'hydro': 2016, 'gas': 7850, 'oil': 329, 'unknown': 192, 'hydro discharge': 254, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 202, 'CZ': 0, 'FR': 1637, 'LU': 0, 'NL': 415, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 744, 'NO-NO2': 687, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 968, 'BE': 512, 'CH': 0, 'CZ': 1580, 'FR': 0, 'LU': 531, 'NL': 0, 'PL': 1564, 'DK-DK1': 55, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 64, 'renewablePercentage': 62, 'powerConsumptionTotal': 59308, 'powerProductionTotal': 60215, 'powerImportTotal': 4302, 'powerExportTotal': 5209, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T20:00:00.000Z', 'updatedAt': '2024-02-21T01:49:42.818Z', 'createdAt': '2024-02-17T20:48:21.810Z', 'powerConsumptionBreakdown': {'nuclear': 1099, 'geothermal': 20, 'biomass': 5062, 'coal': 11734, 'wind': 28170, 'solar': 0, 'hydro': 2685, 'gas': 6983, 'oil': 304, 'unknown': 225, 'hydro discharge': 138, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5590, 'coal': 13192, 'wind': 31030, 'solar': 0, 'hydro': 1900, 'gas': 7761, 'oil': 330, 'unknown': 192, 'hydro discharge': -454, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 0, 'CZ': 0, 'FR': 1405, 'LU': 0, 'NL': 35, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 741, 'NO-NO2': 687, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 1518, 'BE': 472, 'CH': 974, 'CZ': 1603, 'FR': 0, 'LU': 464, 'NL': 0, 'PL': 1429, 'DK-DK1': 168, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 66, 'renewablePercentage': 64, 'powerConsumptionTotal': 56418, 'powerProductionTotal': 60016, 'powerImportTotal': 3484, 'powerExportTotal': 6628, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T21:00:00.000Z', 'updatedAt': '2024-02-21T06:50:16.054Z', 'createdAt': '2024-02-17T21:47:11.494Z', 'powerConsumptionBreakdown': {'nuclear': 984, 'geothermal': 19, 'biomass': 4911, 'coal': 10807, 'wind': 27026, 'solar': 0, 'hydro': 2541, 'gas': 6470, 'oil': 294, 'unknown': 214, 'hydro discharge': 242, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5595, 'coal': 12535, 'wind': 30724, 'solar': 0, 'hydro': 1856, 'gas': 7427, 'oil': 331, 'unknown': 192, 'hydro discharge': 16, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 0, 'CZ': 0, 'FR': 1233, 'LU': 0, 'NL': 0, 'PL': 0, 'DK-DK1': 37, 'DK-DK2': 724, 'NO-NO2': 687, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 2104, 'BE': 864, 'CH': 1510, 'CZ': 1870, 'FR': 0, 'LU': 477, 'NL': 333, 'PL': 1329, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 67, 'renewablePercentage': 65, 'powerConsumptionTotal': 53508, 'powerProductionTotal': 58697, 'powerImportTotal': 3298, 'powerExportTotal': 8486, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T22:00:00.000Z', 'updatedAt': '2024-02-21T06:50:35.325Z', 'createdAt': '2024-02-17T22:49:08.295Z', 'powerConsumptionBreakdown': {'nuclear': 546, 'geothermal': 18, 'biomass': 4773, 'coal': 9802, 'wind': 26008, 'solar': 0, 'hydro': 2326, 'gas': 5987, 'oil': 283, 'unknown': 204, 'hydro discharge': 34, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5607, 'coal': 11706, 'wind': 30494, 'solar': 0, 'hydro': 1813, 'gas': 7122, 'oil': 330, 'unknown': 192, 'hydro discharge': -735, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 0, 'CZ': 0, 'FR': 543, 'LU': 0, 'NL': 0, 'PL': 0, 'DK-DK1': 9, 'DK-DK2': 693, 'NO-NO2': 687, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 2097, 'BE': 931, 'CH': 1876, 'CZ': 1967, 'FR': 0, 'LU': 489, 'NL': 265, 'PL': 1493, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 68, 'renewablePercentage': 66, 'powerConsumptionTotal': 49981, 'powerProductionTotal': 57285, 'powerImportTotal': 2549, 'powerExportTotal': 9118, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-20T23:00:00.000Z', 'updatedAt': '2024-02-21T06:50:16.054Z', 'createdAt': '2024-02-17T23:49:07.838Z', 'powerConsumptionBreakdown': {'nuclear': 990, 'geothermal': 18, 'biomass': 4541, 'coal': 8049, 'wind': 25648, 'solar': 0, 'hydro': 2324, 'gas': 5029, 'oil': 272, 'unknown': 193, 'hydro discharge': 35, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5569, 'coal': 10034, 'wind': 31387, 'solar': 0, 'hydro': 1848, 'gas': 6200, 'oil': 330, 'unknown': 195, 'hydro discharge': -3616, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 0, 'CZ': 0, 'FR': 1352, 'LU': 0, 'NL': 0, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 671, 'NO-NO2': 685, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 1757, 'BE': 826, 'CH': 1732, 'CZ': 1827, 'FR': 0, 'LU': 360, 'NL': 226, 'PL': 1335, 'DK-DK1': 131, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 71, 'renewablePercentage': 69, 'powerConsumptionTotal': 47099, 'powerProductionTotal': 55585, 'powerImportTotal': 3325, 'powerExportTotal': 8195, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-21T00:00:00.000Z', 'updatedAt': '2024-02-21T06:50:07.873Z', 'createdAt': '2024-02-18T00:51:36.182Z', 'powerConsumptionBreakdown': {'nuclear': 1077, 'geothermal': 17, 'biomass': 4331, 'coal': 6936, 'wind': 24846, 'solar': 0, 'hydro': 2195, 'gas': 4787, 'oil': 260, 'unknown': 185, 'hydro discharge': 29, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5536, 'coal': 9012, 'wind': 31677, 'solar': 0, 'hydro': 1854, 'gas': 6140, 'oil': 329, 'unknown': 195, 'hydro discharge': -6127, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 0, 'CZ': 0, 'FR': 1575, 'LU': 0, 'NL': 0, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 657, 'NO-NO2': 654, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 1601, 'BE': 605, 'CH': 1636, 'CZ': 1728, 'FR': 0, 'LU': 324, 'NL': 377, 'PL': 1059, 'DK-DK1': 146, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 73, 'renewablePercentage': 70, 'powerConsumptionTotal': 44664, 'powerProductionTotal': 54765, 'powerImportTotal': 3502, 'powerExportTotal': 7476, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-21T01:00:00.000Z', 'updatedAt': '2024-02-21T06:50:07.873Z', 'createdAt': '2024-02-18T01:48:12.169Z', 'powerConsumptionBreakdown': {'nuclear': 1148, 'geothermal': 17, 'biomass': 4365, 'coal': 6868, 'wind': 23881, 'solar': 0, 'hydro': 2212, 'gas': 4644, 'oil': 264, 'unknown': 185, 'hydro discharge': 19, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5546, 'coal': 8867, 'wind': 30151, 'solar': 0, 'hydro': 1886, 'gas': 5908, 'oil': 332, 'unknown': 195, 'hydro discharge': -6341, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 0, 'CZ': 0, 'FR': 1690, 'LU': 0, 'NL': 0, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 649, 'NO-NO2': 684, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 1675, 'BE': 74, 'CH': 1763, 'CZ': 1636, 'FR': 0, 'LU': 277, 'NL': 76, 'PL': 997, 'DK-DK1': 104, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 73, 'renewablePercentage': 70, 'powerConsumptionTotal': 43604, 'powerProductionTotal': 52907, 'powerImportTotal': 3640, 'powerExportTotal': 6602, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-21T02:00:00.000Z', 'updatedAt': '2024-02-21T06:50:35.325Z', 'createdAt': '2024-02-18T02:56:30.383Z', 'powerConsumptionBreakdown': {'nuclear': 1232, 'geothermal': 17, 'biomass': 4417, 'coal': 7290, 'wind': 24207, 'solar': 0, 'hydro': 2199, 'gas': 4647, 'oil': 270, 'unknown': 185, 'hydro discharge': 15, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5527, 'coal': 9281, 'wind': 30070, 'solar': 0, 'hydro': 1880, 'gas': 5822, 'oil': 333, 'unknown': 195, 'hydro discharge': -5945, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 0, 'CH': 0, 'CZ': 0, 'FR': 1810, 'LU': 0, 'NL': 0, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 648, 'NO-NO2': 686, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 1658, 'BE': 273, 'CH': 1873, 'CZ': 1382, 'FR': 0, 'LU': 272, 'NL': 78, 'PL': 930, 'DK-DK1': 1, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 72, 'renewablePercentage': 69, 'powerConsumptionTotal': 44478, 'powerProductionTotal': 53130, 'powerImportTotal': 3761, 'powerExportTotal': 6467, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-21T03:00:00.000Z', 'updatedAt': '2024-02-21T06:49:44.221Z', 'createdAt': '2024-02-18T03:46:41.338Z', 'powerConsumptionBreakdown': {'nuclear': 1799, 'geothermal': 17, 'biomass': 4439, 'coal': 7624, 'wind': 24105, 'solar': 0, 'hydro': 2311, 'gas': 4822, 'oil': 275, 'unknown': 196, 'hydro discharge': 17, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5491, 'coal': 9611, 'wind': 29235, 'solar': 0, 'hydro': 1866, 'gas': 5859, 'oil': 331, 'unknown': 195, 'hydro discharge': -6226, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 178, 'CH': 0, 'CZ': 0, 'FR': 2651, 'LU': 0, 'NL': 629, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 647, 'NO-NO2': 687, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 1607, 'BE': 0, 'CH': 1447, 'CZ': 1671, 'FR': 0, 'LU': 202, 'NL': 0, 'PL': 1035, 'DK-DK1': 226, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 72, 'renewablePercentage': 68, 'powerConsumptionTotal': 45606, 'powerProductionTotal': 52610, 'powerImportTotal': 5410, 'powerExportTotal': 6188, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-21T04:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T04:49:46.463Z', 'powerConsumptionBreakdown': {'nuclear': 2123, 'geothermal': 18, 'biomass': 4704, 'coal': 9385, 'wind': 24003, 'solar': 0, 'hydro': 2509, 'gas': 5615, 'oil': 294, 'unknown': 220, 'hydro discharge': 20, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5496, 'coal': 11225, 'wind': 27136, 'solar': 0, 'hydro': 1851, 'gas': 6383, 'oil': 331, 'unknown': 195, 'hydro discharge': -3520, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 283, 'CH': 0, 'CZ': 0, 'FR': 2969, 'LU': 0, 'NL': 1182, 'PL': 0, 'DK-DK1': 81, 'DK-DK2': 647, 'NO-NO2': 687, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 1909, 'BE': 0, 'CH': 1053, 'CZ': 1919, 'FR': 0, 'LU': 248, 'NL': 0, 'PL': 1564, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 68, 'renewablePercentage': 64, 'powerConsumptionTotal': 48892, 'powerProductionTotal': 52638, 'powerImportTotal': 6467, 'powerExportTotal': 6693, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-21T05:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T05:47:41.840Z', 'powerConsumptionBreakdown': {'nuclear': 2920, 'geothermal': 20, 'biomass': 5112, 'coal': 11653, 'wind': 25840, 'solar': 0, 'hydro': 2987, 'gas': 6636, 'oil': 321, 'unknown': 281, 'hydro discharge': 935, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5491, 'coal': 12952, 'wind': 26724, 'solar': 0, 'hydro': 1911, 'gas': 6874, 'oil': 331, 'unknown': 196, 'hydro discharge': 368, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 907, 'CH': 133, 'CZ': 0, 'FR': 3600, 'LU': 0, 'NL': 1439, 'PL': 0, 'DK-DK1': 252, 'DK-DK2': 649, 'NO-NO2': 684, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 1853, 'BE': 0, 'CH': 0, 'CZ': 2318, 'FR': 0, 'LU': 340, 'NL': 0, 'PL': 1932, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 67, 'renewablePercentage': 62, 'powerConsumptionTotal': 56705, 'powerProductionTotal': 54868, 'powerImportTotal': 8279, 'powerExportTotal': 6442, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-21T06:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T06:45:17.837Z', 'powerConsumptionBreakdown': {'nuclear': 3320, 'geothermal': 20, 'biomass': 5269, 'coal': 12072, 'wind': 25824, 'solar': 43, 'hydro': 3265, 'gas': 7185, 'oil': 328, 'unknown': 330, 'hydro discharge': 3589, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5478, 'coal': 13099, 'wind': 26252, 'solar': 47, 'hydro': 1897, 'gas': 7309, 'oil': 331, 'unknown': 196, 'hydro discharge': 3739, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 733, 'CH': 1089, 'CZ': 0, 'FR': 3600, 'LU': 0, 'NL': 1497, 'PL': 0, 'DK-DK1': 81, 'DK-DK2': 647, 'NO-NO2': 606, 'SE-SE4': 617}, 'powerExportBreakdown': {'AT': 1361, 'BE': 0, 'CH': 0, 'CZ': 2243, 'FR': 0, 'LU': 458, 'NL': 0, 'PL': 1932, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}, 'fossilFreePercentage': 68, 'renewablePercentage': 62, 'powerConsumptionTotal': 61246, 'powerProductionTotal': 58370, 'powerImportTotal': 8870, 'powerExportTotal': 5994, 'isEstimated': False, 'estimationMethod': None}, {'zone': 'DE', 'datetime': '2024-02-21T07:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T07:47:28.867Z', 'powerConsumptionBreakdown': {'nuclear': 709, 'geothermal': 21, 'biomass': 5435, 'coal': 12422, 'wind': 26185, 'solar': 113, 'hydro': 2674, 'gas': 7211, 'oil': 329, 'unknown': 307, 'hydro discharge': 3705, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5478, 'coal': 13099, 'wind': 26252, 'solar': 47, 'hydro': 1897, 'gas': 7309, 'oil': 331, 'unknown': 196, 'hydro discharge': 3739, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 714, 'CH': 1094, 'CZ': 0, 'LU': 0, 'NL': 1496, 'DK-DK1': 181, 'DK-DK2': 646, 'NO-NO2': 602}, 'powerExportBreakdown': {'AT': 1328, 'BE': 0, 'CH': 0, 'CZ': 2210, 'LU': 455, 'NL': 0, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0}, 'fossilFreePercentage': 66, 'renewablePercentage': 65, 'powerConsumptionTotal': 59111, 'powerProductionTotal': 58370, 'powerImportTotal': 4734, 'powerExportTotal': 3993, 'isEstimated': True, 'estimationMethod': 'TIME_SLICER_AVERAGE'}, {'zone': 'DE', 'datetime': '2024-02-21T08:00:00.000Z', 'updatedAt': '2024-02-21T07:47:25.183Z', 'createdAt': '2024-02-18T08:49:11.590Z', 'powerConsumptionBreakdown': {'nuclear': 260, 'geothermal': 22, 'biomass': 5540, 'coal': 12757, 'wind': 25861, 'solar': 3308, 'hydro': 2103, 'gas': 7161, 'oil': 332, 'unknown': 236, 'hydro discharge': 2523, 'battery discharge': 0}, 'powerProductionBreakdown': {'nuclear': None, 'geothermal': 22, 'biomass': 5466, 'coal': 12929, 'wind': 25507, 'solar': 3319, 'hydro': 1906, 'gas': 7168, 'oil': 325, 'unknown': 197, 'hydro discharge': 2522, 'battery discharge': None}, 'powerImportBreakdown': {'AT': 0, 'BE': 714, 'CH': 1094, 'CZ': 0, 'LU': 0, 'NL': 1496, 'DK-DK1': 181, 'DK-DK2': 646, 'NO-NO2': 602}, 'powerExportBreakdown': {'AT': 1328, 'BE': 0, 'CH': 0, 'CZ': 2210, 'LU': 455, 'NL': 0, 'DK-DK1': 0, 'DK-DK2': 0, 'NO-NO2': 0}, 'fossilFreePercentage': 66, 'renewablePercentage': 65, 'powerConsumptionTotal': 60101, 'powerProductionTotal': 59360, 'powerImportTotal': 4734, 'powerExportTotal': 3993, 'isEstimated': True, 'estimationMethod': 'TIME_SLICER_AVERAGE'}]}



zone: DE
datetime: 2024-02-20T09:00:00.000Z
updatedAt: 2024-02-21T07:47:25.183Z
createdAt: 2024-02-17T09:47:08.464Z
powerConsumptionBreakdown: {'nuclear': 2432, 'geothermal': 20, 'biomass': 5228, 'coal': 13581, 'wind': 17178, 'solar': 11807, 'hydro': 3289, 'gas': 7576, 'oil': 335, 'unknown': 298, 'hydro discharge': 1656, 'battery discharge': 0}
powerProductionBreakdown: {'nuclear': None, 'geothermal': 22, 'biomass': 5391, 'coal': 14718, 'wind': 17813, 'solar': 11883, 'hydro': 2003, 'gas': 7718, 'oil': 329, 'unknown': 192, 'hydro discharge': 1510, 'battery discharge': None}
powerImportBreakdown: {'AT': 0, 'BE': 0, 'CH': 1422, 'CZ': 0, 'FR': 3509, 'LU': 0, 'NL': 1793, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 606, 'NO-NO2': 651}
powerExportBreakdown: {'AT': 888, 'BE': 473, 'CH': 0, 'CZ': 1881, 'FR': 0, 'LU': 373, 'NL': 0, 'PL': 1675, 'DK-DK1': 868, 'DK-DK2': 0, 'NO-NO2': 0}
fossilFreePercentage: 66
renewablePercentage: 62
powerConsumptionTotal: 63400
powerProductionTotal: 61577
powerImportTotal: 7980
powerExportTotal: 6158
isEstimated: False
estimationMethod: None



zone: DE
datetime: 2024-02-20T10:00:00.000Z
updatedAt: 2024-02-21T07:47:25.183Z
createdAt: 2024-02-17T10:50:53.281Z
powerConsumptionBreakdown: {'nuclear': 1820, 'geothermal': 20, 'biomass': 5138, 'coal': 12106, 'wind': 19339, 'solar': 14395, 'hydro': 2889, 'gas': 7277, 'oil': 331, 'unknown': 238, 'hydro discharge': 464, 'battery discharge': 0}
powerProductionBreakdown: {'nuclear': None, 'geothermal': 22, 'biomass': 5443, 'coal': 13153, 'wind': 19842, 'solar': 14617, 'hydro': 1929, 'gas': 7511, 'oil': 330, 'unknown': 192, 'hydro discharge': 285, 'battery discharge': None}
powerImportBreakdown: {'AT': 0, 'BE': 0, 'CH': 181, 'CZ': 0, 'FR': 2765, 'LU': 0, 'NL': 2454, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 749, 'NO-NO2': 685, 'SE-SE4': 292}
powerExportBreakdown: {'AT': 1509, 'BE': 798, 'CH': 0, 'CZ': 1519, 'FR': 0, 'LU': 430, 'NL': 0, 'PL': 1596, 'DK-DK1': 579, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}
fossilFreePercentage: 69
renewablePercentage: 66
powerConsumptionTotal: 64017
powerProductionTotal: 63323
powerImportTotal: 7125
powerExportTotal: 6431
isEstimated: False
estimationMethod: None



zone: DE
datetime: 2024-02-20T11:00:00.000Z
updatedAt: 2024-02-21T07:47:04.377Z
createdAt: 2024-02-17T11:48:16.694Z
powerConsumptionBreakdown: {'nuclear': 1469, 'geothermal': 20, 'biomass': 5134, 'coal': 10522, 'wind': 21857, 'solar': 15049, 'hydro': 2728, 'gas': 6554, 'oil': 322, 'unknown': 209, 'hydro discharge': 52, 'battery discharge': 0}
powerProductionBreakdown: {'nuclear': None, 'geothermal': 22, 'biomass': 5537, 'coal': 11613, 'wind': 22804, 'solar': 15405, 'hydro': 1971, 'gas': 6901, 'oil': 330, 'unknown': 192, 'hydro discharge': -1667, 'battery discharge': None}
powerImportBreakdown: {'AT': 0, 'BE': 2, 'CH': 144, 'CZ': 0, 'FR': 2331, 'LU': 0, 'NL': 2771, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 734, 'NO-NO2': 687, 'SE-SE4': 30}
powerExportBreakdown: {'AT': 1598, 'BE': 0, 'CH': 0, 'CZ': 1879, 'FR': 0, 'LU': 425, 'NL': 0, 'PL': 1646, 'DK-DK1': 341, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}
fossilFreePercentage: 72
renewablePercentage: 70
powerConsumptionTotal: 63915
powerProductionTotal: 64772
powerImportTotal: 6699
powerExportTotal: 5889
isEstimated: False
estimationMethod: None



zone: DE
datetime: 2024-02-20T12:00:00.000Z
updatedAt: 2024-02-21T07:47:19.932Z
createdAt: 2024-02-17T12:46:55.300Z
powerConsumptionBreakdown: {'nuclear': 1836, 'geothermal': 19, 'biomass': 5024, 'coal': 10174, 'wind': 22899, 'solar': 13730, 'hydro': 2728, 'gas': 6345, 'oil': 315, 'unknown': 195, 'hydro discharge': 36, 'battery discharge': 0}
powerProductionBreakdown: {'nuclear': None, 'geothermal': 22, 'biomass': 5575, 'coal': 11470, 'wind': 24338, 'solar': 14013, 'hydro': 2036, 'gas': 6786, 'oil': 330, 'unknown': 192, 'hydro discharge': -1952, 'battery discharge': None}
powerImportBreakdown: {'AT': 0, 'BE': 0, 'CH': 267, 'CZ': 0, 'FR': 3004, 'LU': 0, 'NL': 3318, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 248, 'NO-NO2': 687}
powerExportBreakdown: {'AT': 1676, 'BE': 666, 'CH': 0, 'CZ': 2287, 'FR': 0, 'LU': 357, 'NL': 0, 'PL': 1817, 'DK-DK1': 232, 'DK-DK2': 0, 'NO-NO2': 0}
fossilFreePercentage: 73
renewablePercentage: 70
powerConsumptionTotal: 63299
powerProductionTotal: 64760
powerImportTotal: 7524
powerExportTotal: 7033
isEstimated: False
estimationMethod: None



zone: DE
datetime: 2024-02-20T13:00:00.000Z
updatedAt: 2024-02-21T07:47:04.377Z
createdAt: 2024-02-17T13:50:52.925Z
powerConsumptionBreakdown: {'nuclear': 1854, 'geothermal': 19, 'biomass': 5110, 'coal': 10472, 'wind': 23509, 'solar': 11345, 'hydro': 2801, 'gas': 6257, 'oil': 321, 'unknown': 187, 'hydro discharge': 30, 'battery discharge': 0}
powerProductionBreakdown: {'nuclear': None, 'geothermal': 22, 'biomass': 5599, 'coal': 11749, 'wind': 24886, 'solar': 11469, 'hydro': 2167, 'gas': 6691, 'oil': 330, 'unknown': 192, 'hydro discharge': -1703, 'battery discharge': None}
powerImportBreakdown: {'AT': 0, 'BE': 0, 'CH': 15, 'CZ': 0, 'FR': 3082, 'LU': 0, 'NL': 2855, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 683, 'NO-NO2': 687}
powerExportBreakdown: {'AT': 1866, 'BE': 155, 'CH': 0, 'CZ': 2047, 'FR': 0, 'LU': 397, 'NL': 0, 'PL': 1692, 'DK-DK1': 660, 'DK-DK2': 0, 'NO-NO2': 0}
fossilFreePercentage: 72
renewablePercentage: 69
powerConsumptionTotal: 61907
powerProductionTotal: 63105
powerImportTotal: 7322
powerExportTotal: 6817
isEstimated: False
estimationMethod: None



zone: DE
datetime: 2024-02-20T14:00:00.000Z
updatedAt: 2024-02-21T07:47:25.183Z
createdAt: 2024-02-17T14:44:09.743Z
powerConsumptionBreakdown: {'nuclear': 2240, 'geothermal': 20, 'biomass': 5344, 'coal': 11527, 'wind': 22855, 'solar': 7777, 'hydro': 3064, 'gas': 6720, 'oil': 330, 'unknown': 232, 'hydro discharge': 462, 'battery discharge': 0}
powerProductionBreakdown: {'nuclear': None, 'geothermal': 22, 'biomass': 5639, 'coal': 12536, 'wind': 23560, 'solar': 7465, 'hydro': 2110, 'gas': 7007, 'oil': 330, 'unknown': 192, 'hydro discharge': 255, 'battery discharge': None}
powerImportBreakdown: {'AT': 0, 'BE': 30, 'CH': 351, 'CZ': 0, 'FR': 3252, 'LU': 0, 'NL': 2081, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 719, 'NO-NO2': 687, 'SE-SE4': 161}
powerExportBreakdown: {'AT': 1734, 'BE': 0, 'CH': 0, 'CZ': 2096, 'FR': 0, 'LU': 454, 'NL': 0, 'PL': 1461, 'DK-DK1': 79, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}
fossilFreePercentage: 69
renewablePercentage: 65
powerConsumptionTotal: 60571
powerProductionTotal: 59114
powerImportTotal: 7280
powerExportTotal: 5823
isEstimated: False
estimationMethod: None



zone: DE
datetime: 2024-02-20T15:00:00.000Z
updatedAt: 2024-02-21T07:47:25.183Z
createdAt: 2024-02-17T15:47:56.985Z
powerConsumptionBreakdown: {'nuclear': 3263, 'geothermal': 20, 'biomass': 5547, 'coal': 12637, 'wind': 21875, 'solar': 3529, 'hydro': 3525, 'gas': 7282, 'oil': 332, 'unknown': 340, 'hydro discharge': 1213, 'battery discharge': 1}
powerProductionBreakdown: {'nuclear': None, 'geothermal': 22, 'biomass': 5698, 'coal': 13634, 'wind': 22201, 'solar': 2998, 'hydro': 2059, 'gas': 7490, 'oil': 330, 'unknown': 192, 'hydro discharge': 1157, 'battery discharge': None}
powerImportBreakdown: {'AT': 0, 'BE': 920, 'CH': 1265, 'CZ': 0, 'FR': 3622, 'LU': 0, 'NL': 1329, 'PL': 0, 'DK-DK1': 0, 'DK-DK2': 736, 'NO-NO2': 687, 'SE-SE4': 547}
powerExportBreakdown: {'AT': 1125, 'BE': 0, 'CH': 0, 'CZ': 1997, 'FR': 0, 'LU': 502, 'NL': 0, 'PL': 1547, 'DK-DK1': 151, 'DK-DK2': 0, 'NO-NO2': 0, 'SE-SE4': 0}
fossilFreePercentage: 66
renewablePercentage: 60
powerConsumptionTotal: 59564
powerProductionTotal: 55780
powerImportTotal: 9106
powerExportTotal: 5322
isEstimated: False
estimationMethod: None

.....
.....
.....



---------------------------------------------

