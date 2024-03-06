import time
import requests
from pathlib import Path
from configurator.src.configurator import Configurator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from energy_response_models import Base
from energy_response_models import CarbonIntensityResponse, \
    PowerBreakdownResponse, \
    PowerProductionBreakdown, \
    PowerConsumptionBreakdown, \
    PowerImportBreakdown, \
    PowerExportBreakdown


class APIDataCollectorDBSaver:
    def __init__(self, session, path_url):
        self.session = session
        self.api_base_url = "https://api.electricitymap.org"
        self.path_url = path_url

    def data_collector(self):
        # Make API request to fetch data
        api_response = requests.get(self.api_base_url + self.path_url)
        parsed_json_response = api_response.json()

        return parsed_json_response

    def carbon_intensity_response_saver(self, data: dict):
        carbon_intensity_response = CarbonIntensityResponse(data)

        self.session.add(carbon_intensity_response)
        self.session.commit()
        self.session.close()

    def power_breakdown_response_saver(self, data: dict):
        power_breakdown_response = PowerBreakdownResponse(data)
        # Add power consumption breakdown
        for source, value in data['powerConsumptionBreakdown'].items():
            power_consumption_breakdown = PowerConsumptionBreakdown(source=source, value=value)
            power_breakdown_response.power_consumption_breakdown.append(power_consumption_breakdown)

        # Add power production breakdown
        for source, value in data['powerProductionBreakdown'].items():
            power_production_breakdown = PowerProductionBreakdown(source=source, value=value)
            power_breakdown_response.power_production_breakdown.append(power_production_breakdown)

        # Add power import breakdown
        for source, value in data['powerImportBreakdown'].items():
            power_import_breakdown = PowerImportBreakdown(source=source, value=value)
            power_breakdown_response.power_import_breakdown.append(power_import_breakdown)

        # Add power export breakdown
        for source, value in data['powerExportBreakdown'].items():
            power_export_breakdown = PowerExportBreakdown(source=source, value=value)
            power_breakdown_response.power_export_breakdown.append(power_export_breakdown)

        self.session.add(power_breakdown_response)
        self.session.commit()
        self.session.close()


if __name__ == "__main__":
    general_configurator_path = Path("data/general_config.json")
    general_configurator = Configurator.from_file(str(general_configurator_path))

    # ---------SQLite connection string---------
    # database_connection_string = f'{general_configurator.get_parameter("database_type")}:///' \
    #                              f'{general_configurator.get_parameter("database_name")}'

    # ------PostgreSQL connection string-------
    from sqlalchemy import URL

    url_object = URL.create(drivername='postgresql+psycopg2',
                            username='reza',
                            password='E~1R^5@lGIX0',
                            host='pg-develop2.eb.local',
                            port=5432,
                            database='co2signal')

    database_connection_string = url_object

    # -----database setting-----
    
    engine = create_engine(database_connection_string, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create the table
    Base.metadata.create_all(engine)

    # Create instances
    carbon_intensity_manager = APIDataCollectorDBSaver(session, '/v3/carbon-intensity/latest?zone=DE')
    power_breakdown_manager = APIDataCollectorDBSaver(session, '/v3/power-breakdown/latest?zone=DE')

    # Run indefinitely
    while True:
        # fetch data
        carbon_intensity_data = carbon_intensity_manager.data_collector()
        power_breakdown_data = power_breakdown_manager.data_collector()

        # store data
        carbon_intensity_manager.carbon_intensity_response_saver(carbon_intensity_data)
        power_breakdown_manager.power_breakdown_response_saver(power_breakdown_data)

        # Sleep for 1 hour (3600 seconds)
        time.sleep(3600)
