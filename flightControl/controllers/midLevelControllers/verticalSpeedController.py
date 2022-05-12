from flightControl.compoents.controller import Controller
from flightControl.controllers.lowLevelControllers.pitchController import PitchController


class VerticalSpeedController(Controller):
    # feed:VerticalSpeed out:pitch
    default_min_output = -30
    default_max_output = 30

    def __init__(self, interface, logger):
        super().__init__("VerticalSpeedController", interface, logger, self.default_min_output,
                         self.default_max_output)
        self.elevatorController = PitchController(interface, logger)
        self.current_altitude = self.interface.altitude
        self.last_altitude = 0
        self.current_vs = 0
        self.last_vs = 0
        self.pid.tunings = (1.5, 0.05, 0.01)

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
