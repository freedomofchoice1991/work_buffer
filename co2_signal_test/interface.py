import multiprocessing
import signal
import time
import os
import sys
from server_script import APIDataCollectorDBSaver
import logging
from system_calls import SystemCallsManager

shell_pid = os.getppid()

class CO2SignalInterface:
    def __init__(self):
        self.server_script = APIDataCollectorDBSaver()
        self.server_process = None
        parent_signal_catcher = SystemCallsManager(os.getpid())
        logging.info(f"Parent process {os.getpid()} has been created...\n")


    def start_server_script(self):
        self.server_process = multiprocessing.Process(target=self.server_script.fetch_and_store_data, )
        self.server_process.start()
        #message = f'Server process:{os.getpid()} is running....'
        #logging.info(message)

    def stop_server_script(self):
        if self.server_process:
            self.server_process.terminate()
            #message = f'Server process:{os.getpid()} has stopped....'
            #logging.info(message)





if __name__ == "__main__":
    logging.basicConfig(filename='logs.log', filemode='a', level=logging.INFO,
                        format='%(filename)s - %(lineno)d - %(asctime)s - %(levelname)s - %(message)s')
    logging.info(f'Program is started in a shell process with id: {shell_pid}')

    #parent_signal_catcher = SystemCallsManager(os.getpid())
    #message = f'Parent process {os.getpid()} has been created...'
    
    interface_instance = CO2SignalInterface()
    interface_instance.start_server_script()
    
