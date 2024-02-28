import multiprocessing


class ProcessManager:
    def __init__(self, requests: list):
        self.requests = requests
        self.processes: list = []

    def start(self):
        for request in self.requests:
            process = multiprocessing.Process(target=request.report, )

            self.processes.append(process)
            process.start()

        for process in self.processes:
            process.join()
