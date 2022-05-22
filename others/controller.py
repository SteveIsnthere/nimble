from abc import abstractmethod

from others.simple_pid import PID
from others.helpers import Helpers


class Controller:
    lastUpdateTime = None
    lastReadDataTime = None
    output = 0
    lastOutput = 0
    targetReading = None
    currentReading = None
    lastReading = 0

    @property
    def delta_time(self):
        return self.currentTime - self.lastUpdateTime

    @property
    def fetch_data_delta_time(self):
        return self.currentTime - self.lastReadDataTime

    @property
    def fetch_data_time_interval(self):
        return 1/self.fetch_data_frequency

    def __init__(self, name, interface, logger, min_output, max_output):
        self.currentTime = Helpers.time()
        self.name = name
        self.id = Helpers.uuid()
        self.interface = interface
        self.logger = logger
        self.lastUpdateTime = self.currentTime - 0.001
        self.lastReadDataTime = self.currentTime - 0.001
        self.minOutput = min_output
        self.maxOutput = max_output
        self.pid = PID(0.13, 0.01, 0.01)
        self.pid.output_limits = (min_output, max_output)
        self.fetch_data_frequency = self.interface.DEFAULT_FETCH_DATA_FREQUENCY

    def update(self, target_reading):
        self.lastUpdateTime = self.currentTime
        self.currentTime = Helpers.time()

        self.fetch_data_and_generate_output(target_reading)
        self.apply_output(self.output)

    def fetch_data_and_generate_output(self,target_reading):
        if self.fetch_data_delta_time > self.fetch_data_time_interval:
            self.currentReading = self.get_current_reading()
            self.targetReading = target_reading
            self.output = self.get_output()
            self.lastOutput = self.output
            self.lastReading = self.currentReading
            self.lastReadDataTime = self.currentTime

    def get_output(self):
        self.pid.sample_time = self.fetch_data_delta_time
        self.pid.set_point = self.targetReading
        output = self.pid(self.currentReading)
        return output

    @abstractmethod
    def get_current_reading(self):
        pass

    @abstractmethod
    def apply_output(self, output):
        pass

    def reset(self):
        self.pid.reset()

    def log_data(self, data_type, content):
        self.logger.update(self.name, data_type, content)
