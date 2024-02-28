from electricity_maps import ElectricityMaps
from multi_processing import ProcessManager
from pathlib import Path
from configurator.src.configurator import Configurator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from energy_response_models import Base

if __name__ == "__main__":
    # -----create Configurator-----
    general_configurator_path = Path("data/general_config.json")
    general_configurator = Configurator.from_file(str(general_configurator_path))

    # -----prepare objects for multiprocessing-----
    # getting data from configuration file
    auth_token = general_configurator.get_parameter("authentication_token")
    estimated_data = general_configurator.get_parameter("estimated_data")
    database_name = general_configurator.get_parameter("database_name")
    database_type = general_configurator.get_parameter("database_type")
    database_connection_string = f'{database_type}:///{database_name}'

    # -----database setting-----
    engine = create_engine(database_connection_string, echo=False)
    Base.metadata.create_all(bind=engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # creating objects to pass to multiprocessing
    report1 = ElectricityMaps(auth_token,
                              "latest",
                              "carbon-intensity",
                              database_connection_string,
                              estimated_data)

    report2 = ElectricityMaps(auth_token,
                              "latest",
                              "power-breakdown",
                              database_connection_string,
                              estimated_data)

    report3 = ElectricityMaps(auth_token,
                              "history",
                              "carbon-intensity",
                              database_connection_string,
                              estimated_data)

    report4 = ElectricityMaps(auth_token,
                              "history",
                              "power-breakdown",
                              database_connection_string,
                              estimated_data)

    report_requests = [report1, report2, report3, report4]
    mp = ProcessManager(report_requests)
    mp.start()
