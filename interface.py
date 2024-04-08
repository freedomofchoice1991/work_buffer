import multiprocessing
import time

from server_script import APIDataCollectorDBSaver
import logging


class CO2SignalInterface:
    def __init__(self):
        self.server_script = APIDataCollectorDBSaver()
        self.server_process = None

    def start_server_script(self):
        self.server_process = multiprocessing.Process(target=self.server_script.fetch_and_store_data, )
        self.server_process.start()
        message = 'Server process is running....'
        logging.info(message)

    def stop_server_script(self):
        if self.server_process:
            self.server_process.terminate()
            message = 'Server process has stopped....'
            logging.info(message)


if __name__ == "__main__":
    logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG,
                        format='%(filename)s - %(lineno)d - %(asctime)s - %(levelname)s - %(message)s')

    interface_instance = CO2SignalInterface()
    interface_instance.start_server_script()
