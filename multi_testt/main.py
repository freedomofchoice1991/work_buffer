import multiprocessing
import logging
import time
import signal
import os
from system_calls import SystemCallsManager




program_pid = os.getppid()

class MultiprocessingExample:
    def __init__(self, num_processes):
        main_process_signal_listener = SystemCallsManager(os.getpid())  # This line sets a systemcallmanager for the parent process
        self.num_processes = num_processes
        self.parent_id = os.getpid()
        self.processes = []

    def worker(self, name):
        sub_process_signal_listener = SystemCallsManager(os.getpid())     # This line sets a systemcallmanager for this process (basically each child process)
        for i in range(150):
            print(f"Worker {name} started, PID: {os.getpid()}  -  parent_id : {self.parent_id}")
            time.sleep(7)


    def run(self):
        for i in range(self.num_processes):
            process = multiprocessing.Process(target=self.worker, args=(f'Process-{i}',))
            self.processes.append(process)
            process.start()
        for process in self.processes:
            process.join()

if __name__ == '__main__':
    logging.basicConfig(filename='logs.log', filemode='a', level=logging.INFO,
                        format='%(filename)s - %(lineno)d - %(asctime)s - %(levelname)s - %(message)s')
    print(f'=================shell process id: {program_pid}')
    example = MultiprocessingExample(num_processes=2)
    example.run()


