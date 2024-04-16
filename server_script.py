import time
import requests
from pathlib import Path
from contextlib import contextmanager
from configurator.src.configurator import Configurator
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from energy_response_models import Base
from energy_response_models import Power, PowerPlant, Emission, Location, DataSource
from datetime import datetime
from datetime import timedelta
from sqlalchemy import URL


class APIDataCollectorDBSaver:
    def __init__(self):
        self.api_base_url = "https://api.electricitymap.org"

    @contextmanager
    def session_scope(self):
        general_configurator_path = Path("data/general_config.json")
        general_configurator = Configurator.from_file(str(general_configurator_path))

        # ------PostgreSQL connection string-------
        url_object = URL.create(drivername=general_configurator.get_parameter("database_drivername"),
                                username=general_configurator.get_parameter("database_username"),
                                password=general_configurator.get_parameter("database_password"),
                                host=general_configurator.get_parameter("database_host"),
                                port=general_configurator.get_parameter("database_port"),
                                database=general_configurator.get_parameter("database_name"))

        database_connection_string = url_object
        # ------PostgreSQL TEST connection string-------
        # url_object = URL.create(drivername='postgresql+psycopg2',
        #                         username='postgres',
        #                         password='adminpass',
        #                         host='localhost',
        #                         port=5432,
        #                         database='co2signal_test')
        #
        # database_connection_string = url_object
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
            location = Location(country=location_data)
            last_row = session.query(Location).order_by(desc(Location.id)).first()

            if last_row is None or last_row.country != location_data:
                session.add(location)

    def datasource_saver(self, name):
        with self.session_scope() as session:
            data_source = DataSource(data_source_name=name, data_source_link=self.api_base_url)
            last_row = session.query(DataSource).order_by(desc(DataSource.id)).first()

            if last_row is None or last_row.data_source_name != name:
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

    def power_plant_saver(self, location_id, data_source_id):
        with self.session_scope() as session:
            pp1 = PowerPlant(power_plant_name='Germany',
                             power_plant_type='nuclear', production_status=True,
                             renewable_energy_status=True, high_carbon_source_status=False,
                             location_id=location_id, data_source_id=data_source_id)
            pp2 = PowerPlant(power_plant_name='Germany', power_plant_type='geothermal', production_status=True,
                             renewable_energy_status=True, high_carbon_source_status=False,
                             location_id=location_id, data_source_id=data_source_id)
            pp3 = PowerPlant(power_plant_name='Germany', power_plant_type='biomass', production_status=True,
                             renewable_energy_status=True, high_carbon_source_status=True,
                             location_id=location_id, data_source_id=data_source_id)
            pp4 = PowerPlant(power_plant_name='Germany', power_plant_type='coal', production_status=True,
                             renewable_energy_status=False, high_carbon_source_status=True,
                             location_id=location_id, data_source_id=data_source_id)
            pp5 = PowerPlant(power_plant_name='Germany', power_plant_type='wind', production_status=True,
                             renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                             data_source_id=data_source_id)
            pp6 = PowerPlant(power_plant_name='Germany', power_plant_type='solar', production_status=True,
                             renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                             data_source_id=data_source_id)
            pp7 = PowerPlant(power_plant_name='Germany', power_plant_type='hydro', production_status=True,
                             renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                             data_source_id=data_source_id)
            pp8 = PowerPlant(power_plant_name='Germany', power_plant_type='gas', production_status=True,
                             renewable_energy_status=False, high_carbon_source_status=True, location_id=location_id,
                             data_source_id=data_source_id)
            pp9 = PowerPlant(power_plant_name='Germany', power_plant_type='oil', production_status=True,
                             renewable_energy_status=False, high_carbon_source_status=True, location_id=location_id,
                             data_source_id=data_source_id)
            pp10 = PowerPlant(power_plant_name='Germany', power_plant_type='unknown', production_status=True,
                              renewable_energy_status=None, high_carbon_source_status=None, location_id=location_id,
                              data_source_id=data_source_id)
            pp11 = PowerPlant(power_plant_name='Germany', power_plant_type='hydro discharge', production_status=True,
                              renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                              data_source_id=data_source_id)
            pp12 = PowerPlant(power_plant_name='Germany', power_plant_type='battery discharge', production_status=True,
                              renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                              data_source_id=data_source_id)

            pp13 = PowerPlant(power_plant_name='Germany', power_plant_type='nuclear', production_status=False,
                              renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                              data_source_id=data_source_id)
            pp14 = PowerPlant(power_plant_name='Germany', power_plant_type='geothermal', production_status=False,
                              renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                              data_source_id=data_source_id)
            pp15 = PowerPlant(power_plant_name='Germany', power_plant_type='biomass', production_status=False,
                              renewable_energy_status=True, high_carbon_source_status=True, location_id=location_id,
                              data_source_id=data_source_id)
            pp16 = PowerPlant(power_plant_name='Germany', power_plant_type='coal', production_status=False,
                              renewable_energy_status=False, high_carbon_source_status=True, location_id=location_id,
                              data_source_id=data_source_id)
            pp17 = PowerPlant(power_plant_name='Germany', power_plant_type='wind', production_status=False,
                              renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                              data_source_id=data_source_id)
            pp18 = PowerPlant(power_plant_name='Germany', power_plant_type='solar', production_status=False,
                              renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                              data_source_id=data_source_id)
            pp19 = PowerPlant(power_plant_name='Germany', power_plant_type='hydro', production_status=False,
                              renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                              data_source_id=data_source_id)
            pp20 = PowerPlant(power_plant_name='Germany', power_plant_type='gas', production_status=False,
                              renewable_energy_status=False, high_carbon_source_status=True, location_id=location_id,
                              data_source_id=data_source_id)
            pp21 = PowerPlant(power_plant_name='Germany', power_plant_type='oil', production_status=False,
                              renewable_energy_status=False, high_carbon_source_status=True, location_id=location_id,
                              data_source_id=data_source_id)
            pp22 = PowerPlant(power_plant_name='Germany', power_plant_type='unknown', production_status=False,
                              renewable_energy_status=None, high_carbon_source_status=None, location_id=location_id,
                              data_source_id=data_source_id)
            pp23 = PowerPlant(power_plant_name='Germany', power_plant_type='hydro discharge', production_status=False,
                              renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                              data_source_id=data_source_id)
            pp24 = PowerPlant(power_plant_name='Germany', power_plant_type='battery discharge', production_status=False,
                              renewable_energy_status=True, high_carbon_source_status=False, location_id=location_id,
                              data_source_id=data_source_id)
            virtual_power_plants = [pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12,
                                    pp13, pp14, pp15, pp16, pp17, pp18, pp19, pp20, pp21, pp22, pp23, pp24]
            first_row = session.query(PowerPlant).first()
            if first_row is None:
                session.add_all(virtual_power_plants)

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
                for source, value in item['powerConsumptionBreakdown'].items():
                    records = session.query(PowerPlant).filter(PowerPlant.production_status == 'False').all()
                    for record in records:
                        if record.power_plant_type == source:
                            pp_id = record.id
                    consumed_power = Power(amount=value,
                                           date_time=datetime.strptime(item['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
                                           power_plant_id=pp_id,
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
                                           power_plant_id=pp_id,
                                           data_source_id=source_id)

                    if produced_power not in last_24_hours_rows:
                        session.add(produced_power)

    def fetch_and_store_data(self):
        self.location_saver(location_data='DE')
        self.datasource_saver('Electricity Maps')
        with self.session_scope() as session:
            source = session.query(DataSource).first()
            data_source_id = source.id
            location = session.query(Location).first()
            location_id = location.id
            self.power_plant_saver(location_id, data_source_id)

        while True:
            carbon_intensity_data = self.data_collector('/v3/carbon-intensity/history?zone=DE')
            power_breakdown_data = self.data_collector('/v3/power-breakdown/history?zone=DE')

            self.carbon_intensity_response_saver(carbon_intensity_data)
            self.power_saver(power_breakdown_data)

            # Sleep for 1 hour (3600 seconds)
            time.sleep(3600)
