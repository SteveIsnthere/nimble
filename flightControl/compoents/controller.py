from flightControl.compoents.simple_pid import PID

from util.helpers import Helpers


class Controller:
    lastUpdateTime = None
    lastOutput = 0
    targetReading = None
    currentReading = None
    lastReading = 0

    @property
    def delta_time(self):
        return self.currentTime - self.lastUpdateTime

    def __init__(self, name, interface, logger, min_output, max_output):
        self.currentTime = Helpers.time()
        self.name = name
        self.id = Helpers.uuid()
        self.interface = interface
        self.logger = logger
        self.lastUpdateTime = self.currentTime - 0.01
        self.minOutput = min_output
        self.maxOutput = max_output
        self.pid = PID(0.13, 0.01, 0.01)
        self.pid.output_limits = (min_output, max_output)

    def update(self, target_reading):
        self.currentReading = self.get_current_reading()
        self.targetReading = target_reading
        self.update_time()
        output = self.get_output()
        self.apply_output(output)
        self.lastOutput = output
        self.lastReading = self.currentReading

    def get_output(self):
        self.pid.sample_time = self.delta_time
        self.pid.set_point = self.targetReading
        output = self.pid(self.currentReading)
        return output

    def update_time(self):
        self.lastUpdateTime = self.currentTime
        self.currentTime = Helpers.time()

    def get_current_reading(self):
        raise Exception('please override this method')

    def apply_output(self, output):
        raise Exception('please override this method')

    def log_data(self, data_type, content):
        self.logger.update(self.name, data_type, content)
