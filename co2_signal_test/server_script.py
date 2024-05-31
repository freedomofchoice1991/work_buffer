import signal
import logging
import os
import time
import requests
from pathlib import Path
from contextlib import contextmanager
from configurator.src.configurator import Configurator
from sqlalchemy import create_engine, desc, text
from sqlalchemy.orm import sessionmaker
from energy_response_models import Base
from energy_response_models import Power, PowerPlant, Emission, Location, DataSource
from datetime import datetime
from datetime import timedelta
from sqlalchemy import URL
from system_calls import SystemCallsManager


class APIDataCollectorDBSaver:
    def __init__(self):
        self.api_base_url = "https://api.electricitymap.org"
    

    @contextmanager
    def session_scope(self):
        general_configurator_path = Path("data/general_config.json")
        general_configurator = Configurator.from_file(str(general_configurator_path))


        url_object = URL.create(drivername='postgresql+psycopg2',
                                username='reza',
                                password='E~1R^5@lGIX0',
                                host='pg-develop2.eb.local',
                                port=5432,
                                database='co2signal_test')

        database_connection_string = url_object
        # -----database setting-----
        connection_engine = create_engine(database_connection_string)
        Session = sessionmaker(bind=connection_engine)
        transaction_session = Session()
        Base.metadata.create_all(connection_engine)
        try:
            yield transaction_session
            transaction_session.commit()
        except KeyboardInterrupt:
            transaction_session.rollback()
            raise ValueError('Interruption happened while connecting to DB.')
        finally:
            transaction_session.close()
            connection_engine.dispose()

    def data_collector(self, path_url):
        parsed_json_response = None
        try:
            # Make API request to fetch data
            api_response = requests.get(self.api_base_url + path_url)
            parsed_json_response = api_response.json()
        except requests.RequestException as error:
            print('Error making request:', error)
        return parsed_json_response

    def location_saver(self, location_data):
        with self.session_scope() as session:
            location_records = session.query(Location).filter(Location.country_name == None).all()
            for key, value in location_data.items():
                for record in location_records:
                    if key == record.country_code:
                        record.country_name = value.get('zoneName')

    def datasource_saver(self, name):
        with self.session_scope() as session:
            data_source = DataSource(data_source_name=name, data_source_link=self.api_base_url)
            data_source_names_records = session.query(DataSource.data_source_name).all()
            data_sources_names = [row[0] for row in data_source_names_records]  # extract names as list
            # if the table is empty or this is a new name then insert as new data source
            if len(data_source_names_records) == 0 or name not in data_sources_names:
                session.add(data_source)

    def carbon_intensity_response_saver(self, data: dict):
        with self.session_scope() as session:
            history_list = data['history']
            power_plant = session.query(PowerPlant).first()
            plant_id = power_plant.id
            source = session.query(DataSource).first()
            source_id = source.id
            last_row = session.query(Emission).order_by(desc(Emission.id)).first()
            most_recent_time = last_row.date_time if last_row else None

            # If there are no emissions yet, consider the most recent time as None
            if most_recent_time:
                start_time = most_recent_time - timedelta(hours=24)
            else:
                start_time = None

            # If there are no emissions yet, there's no end time to consider
            end_time = most_recent_time if most_recent_time else None

            last_24_hours_rows = []
            # If there are emissions in the last 24 hours, query them
            if start_time and end_time:
                last_24_hours_rows = session.query(Emission).filter(
                    Emission.date_time.between(start_time, end_time)).all()

            for item in history_list:
                emission = Emission(emission_type='CO2',
                                    emission_amount=item['carbonIntensity'],
                                    calculation_method=item['emissionFactorType'],
                                    data_estimation=item['isEstimated'],
                                    date_time=datetime.strptime(item['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                                    power_plant_id=plant_id,
                                    data_source_id=source_id)

                for row in last_24_hours_rows:
                    if emission == row:
                        break
                # This else is associated with for loop and executes only if the loop completes normally
                else:
                    session.add(emission)

    def power_plant_saver(self, location_data, data_source_id):
        with self.session_scope() as session:
            Germany_location = session.query(Location).filter(Location.country_code == 'DE').first()
            Germany_location_id = Germany_location.id
            data_source_id = data_source_id

            power_plant_configurator_path = Path("data/power_plant_config.json")
            power_plant_configurator = Configurator.from_file(str(power_plant_configurator_path))
            virtual_power_plants_data = power_plant_configurator.get_parameter("virtual_power_plants_data")
            virtual_power_plants = []
            for plant_data in virtual_power_plants_data:
                pp = PowerPlant(
                    power_plant_type=plant_data["power_plant_type"],
                    production_status=plant_data["production_status"],
                    renewable_energy_status=plant_data["renewable_energy_status"],
                    high_carbon_source_status=plant_data["high_carbon_source_status"],
                    location_id=Germany_location_id,
                    data_source_id=data_source_id
                )
                virtual_power_plants.append(pp)

            number_of_existing_rows = session.query(PowerPlant).count()
            # Add virtual power_plants only if the table is empty
            if number_of_existing_rows == 0:
                session.add_all(virtual_power_plants)

            real_power_plants = []
            for country_code, country_info in location_data.items():
                if country_code == 'DE':
                    continue
                pp_type = 'Unknown'
                pp_location = session.query(Location).filter(Location.country_code == country_code).first()
                pp_location_id = pp_location.id
                real_power_plant = PowerPlant(power_plant_type=pp_type,
                                              location_id=pp_location_id,
                                              data_source_id=data_source_id)
                real_power_plants.append(real_power_plant)

            # add real power_plants only once
            existing_power_plants_count = session.query(PowerPlant).count()
            if existing_power_plants_count == 24:
                session.add_all(real_power_plants)

    def power_saver(self, data: dict):
        with self.session_scope() as session:
            source = session.query(DataSource).first()
            source_id = source.id
            history_list = data['history']
            last_row = session.query(Power).order_by(desc(Power.id)).first()
            most_recent_time = last_row.date_time if last_row else None

            # If there are no power entity yet, consider the most recent time as None
            if most_recent_time:
                start_time = most_recent_time - timedelta(hours=24)
            else:
                start_time = None

            # If there are no power entity yet, there's no end time to consider
            end_time = most_recent_time if most_recent_time else None

            last_24_hours_rows = []
            # If there are power entities in the last 24 hours, query them
            if start_time and end_time:
                last_24_hours_rows = session.query(Power).filter(
                    Power.date_time.between(start_time, end_time)).all()

            for item in history_list:
                # ---- Production Consumption section -----
                for source, value in item['powerConsumptionBreakdown'].items():
                    records = session.query(PowerPlant).filter(PowerPlant.production_status == 'False').all()
                    for record in records:
                        if record.power_plant_type == source:
                            pp_id = record.id
                    consumed_power = Power(amount=value,
                                           date_time=datetime.strptime(item['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                                           source_power_plant_id=pp_id,
                                           data_source_id=source_id)
                    for row in last_24_hours_rows:
                        if consumed_power == row:
                            break
                    else:
                        session.add(consumed_power)

                for source, value in item['powerProductionBreakdown'].items():
                    records = session.query(PowerPlant).filter(PowerPlant.production_status == 'True').all()
                    for record in records:
                        if record.power_plant_type == source:
                            pp_id = record.id
                    produced_power = Power(amount=value,
                                           date_time=datetime.strptime(item['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                                           source_power_plant_id=pp_id,
                                           data_source_id=source_id)

                    if produced_power not in last_24_hours_rows:
                        session.add(produced_power)
                #  ---- Import Export section -----
                existing_locations = session.query(Location).all()
                existing_power_plants = session.query(PowerPlant).all()
                destination_power_plant_id = None
                for source, value in item['powerImportBreakdown'].items():
                    # find the location rows for both import_source and import_destination
                    for location in existing_locations:
                        if source == location.country_code:
                            import_source_location = location
                            import_source_location_id = import_source_location.id
                        elif item['zone'] == location.country_code:
                            import_destination_location = location
                            import_destination_location_id = import_destination_location.id
                    # find the power_plant rows based on import_source_location_id and import_destination_location_id
                    for power_plant in existing_power_plants:
                        if power_plant.location_id == import_source_location_id:
                            source_power_plant_id = power_plant.location_id
                        elif power_plant.location_id == import_destination_location_id:
                            destination_power_plant_id = power_plant.location_id
                    # create the Power object
                    imported_power = Power(amount=value,
                                           date_time=datetime.strptime(item['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                                           source_power_plant_id=source_power_plant_id,
                                           destination_power_plant_id=destination_power_plant_id,
                                           data_source_id=source_id)
                    # add it into DB if not there already
                    if imported_power not in last_24_hours_rows:
                        session.add(imported_power)

                for source, value in item['powerExportBreakdown'].items():
                    # find the location rows for both export_source and export_destination
                    for location in existing_locations:
                        if source == location.country_code:
                            export_destination_location = location
                            export_destination_location_id = export_destination_location.id
                        elif item['zone'] == location.country_code:
                            export_source_location = location
                            export_source_location_id = export_source_location
                    # find the power_plant rows based on export_destination_location_id and export_source_location_id
                    for power_plant in existing_power_plants:
                        if power_plant.location_id == export_destination_location_id:
                            destination_power_plant_id = power_plant.location_id
                        elif power_plant.location_id == export_source_location_id:
                            source_power_plant_id = power_plant.location_id
                    # create the Power object
                    exported_power = Power(amount=value,
                                           date_time=datetime.strptime(item['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                                           source_power_plant_id=source_power_plant_id,
                                           destination_power_plant_id=destination_power_plant_id,
                                           data_source_id=source_id)
                    # add it into DB if not there already
                    if exported_power not in last_24_hours_rows:
                        session.add(exported_power)

    def fetch_and_store_data(self):
        child_system_catcher = SystemCallsManager(os.getpid())
        message = f"Child process: {os.getpid()} is running...Parent of this child:{os.getppid()}"
        logging.info(message)
        WAITING_TIME = 1
        location_data = self.data_collector('/v3/zones')
        self.location_saver(location_data=location_data)
        self.datasource_saver('Electricity Maps')
        with self.session_scope() as session:
            source = session.query(DataSource).first()
            data_source_id = source.id
            self.power_plant_saver(location_data, data_source_id)

        while True:
            current_time = datetime.now()
            with self.session_scope() as session:
                recent_emission_record = session.query(Emission).order_by(desc(Emission.id)).first()
                last_data_fetch_time = recent_emission_record.date_time

            time_difference = current_time - last_data_fetch_time

            if time_difference >= timedelta(hours=1):
                carbon_intensity_data_life_cycle_emission_factor =\
                    self.data_collector('/v3/carbon-intensity/history?zone=DE')
                carbon_intensity_data_direct_emission_factor =\
                    self.data_collector('/v3/carbon-intensity/history?zone=DE&emissionFactorType=direct')
                power_breakdown_data = self.data_collector('/v3/power-breakdown/history?zone=DE')

                self.carbon_intensity_response_saver(carbon_intensity_data_life_cycle_emission_factor)
                self.carbon_intensity_response_saver(carbon_intensity_data_direct_emission_factor)
                self.power_saver(power_breakdown_data)

            time.sleep(WAITING_TIME)
