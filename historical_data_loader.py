from energy_response_models import Emission, PowerPlant, DataSource
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import URL
from server_script import Base
import csv
from pathlib import Path
from server_script import APIDataCollectorDBSaver
import logging
from configurator.src.configurator import Configurator


class HistoricalDataLoader:
    def __init__(self, driver_name, username, password, host, port, database_name, data_source_name,
                 historical_data_path):
        self.driver_name = driver_name
        self.username = username
        self.password = password
        self.host_name = host
        self.port_number = port
        self.database_name = database_name
        self.data_source_name = data_source_name
        self.historical_data = historical_data_path
        self.database_connection_string = URL.create(self.driver_name,
                                                     self.username,
                                                     self.password,
                                                     self.host_name,
                                                     self.port_number,
                                                     self.database_name)
        self.connection_engine = create_engine(self.database_connection_string)
        Session = sessionmaker(bind=self.connection_engine)
        self.session = Session()
        Base.metadata.create_all(self.connection_engine)

    def add_new_data_source(self):
        source_maker = APIDataCollectorDBSaver()
        source_maker.datasource_saver(self.data_source_name)
        message = f'The new data source "{self.data_source_name}" has been added...\n\n\n'
        logging.info(message)

    def prepare_emission_records(self):

        with (open(self.historical_data, 'r') as historical_data_csv_file):
            reader = csv.DictReader(historical_data_csv_file)

            historical_emission_data = []

            for row in reader:
                emission_basic_structure = {'emission_type': 'CO2',
                                            'emission_amount': None,
                                            'calculation_method': None,
                                            'data_estimation': bool(row['Data Estimation Method'].capitalize()),
                                            'date_time': str(row['Datetime (UTC)'])}

                lca_dict = emission_basic_structure.copy()
                lca_dict['emission_amount'] = row['Carbon Intensity gCOâ‚‚eq/kWh (LCA)']
                lca_dict['calculation_method'] = 'lifecycle'

                direct_dict = emission_basic_structure.copy()
                direct_dict['emission_amount'] = row['Carbon Intensity gCOâ‚‚eq/kWh (direct)']
                direct_dict['calculation_method'] = 'direct'

                historical_emission_data.append(lca_dict)
                historical_emission_data.append(direct_dict)
        return historical_emission_data

    def create_emission_objects(self, emit_data: list):
        power_plant = self.session.query(PowerPlant).first()
        source = self.session.query(DataSource).filter(DataSource.data_source_name == self.data_source_name).first()
        emission_records = []
        for data in emit_data:
            emission_record = Emission(emission_type=data.get('emission_type'),
                                       emission_amount=data.get('emission_amount'),
                                       calculation_method=data.get('calculation_method'),
                                       data_estimation=data.get('data_estimation'),
                                       date_time=data.get('date_time'),
                                       power_plant_id=power_plant.id,
                                       data_source_id=source.id)
            emission_records.append(emission_record)
        return emission_records

    def insert_emissions(self, emission_records: list):
        self.session.add_all(emission_records)
        self.session.commit()
        self.session.close()


if __name__ == '__main__':
    logging.basicConfig(filename='historical_data_insertion_logs.log', filemode='w', level=logging.DEBUG,
                        format='%(filename)s - %(lineno)d - %(asctime)s - %(levelname)s - %(message)s')
    general_configurator_path = Path("data/general_config.json")
    historical_data_configurator_path = Path("data/historical_data_config.json")
    general_configurator = Configurator.from_file(str(general_configurator_path))
    historical_data_configurator = Configurator.from_file(str(historical_data_configurator_path))

    data_loader = HistoricalDataLoader(general_configurator.get_parameter("database_drivername"),
                                       general_configurator.get_parameter("database_username"),
                                       general_configurator.get_parameter("database_password"),
                                       general_configurator.get_parameter("database_host"),
                                       general_configurator.get_parameter("database_port"),
                                       general_configurator.get_parameter("database_name"),
                                       historical_data_configurator.get_parameter("data_source_name"),
                                       # for each year do separately  2021, 2022, 2023
                                       # and FIRST ADD DATA FILES to Project
                                       historical_data_configurator.get_parameter("historical_2021_data_path"))
    data_loader.add_new_data_source()
    emissions_data = data_loader.prepare_emission_records()
    emissions = data_loader.create_emission_objects(emissions_data)
    data_loader.insert_emissions(emissions)
