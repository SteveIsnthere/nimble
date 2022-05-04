from flightControl.compoents.controller import Controller
from flightControl.lowLevelControllers.elevatorController import ElevatorController


class VerticalSpeedController(Controller):
    # feed:VerticalSpeed out:pitch
    default_min_output = -50
    default_max_output = 35

    def __init__(self, interface, logger):
        super().__init__("VerticalSpeedController", interface, logger, self.default_min_output,
                         self.default_max_output)
        self.elevatorController = ElevatorController(interface, logger)
        self.current_altitude = self.interface.altitude
        self.last_altitude = 0
        self.current_vs = 0
        self.last_vs = 0
        self.pid.tunings = (2, 0.1, 0.02)

    def get_current_reading(self):
        self.last_altitude = self.current_altitude
        self.current_altitude = self.interface.altitude
        self.last_vs = self.current_vs
        self.current_vs = (self.current_altitude - self.last_altitude) / self.delta_time
        self.current_vs = (self.last_vs * 29 + self.current_vs) / 30
        return self.current_vs

    def apply_output(self, output):
        self.log_data("reading", self.currentReading)
        self.log_data("output", output)
        self.elevatorController.update(output)
