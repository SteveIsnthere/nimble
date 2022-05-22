from others.controller import Controller
from flightControl.controllers.lowLevelControllers.pitchController import PitchController


class VerticalSpeedController(Controller):
    # feed:VerticalSpeed out:pitch
    default_min_output = -30
    default_max_output = 30

    def __init__(self, interface, logger):
        super().__init__("VerticalSpeedController", interface, logger, self.default_min_output,
                         self.default_max_output)
        self.elevatorController = PitchController(interface, logger)
        self.pid.tunings = (1.5, 0.05, 0.01)
        self.fetch_data_frequency = self.interface.BAROMETER_FETCH_DATA_FREQUENCY

    def get_current_reading(self):
        return self.interface.vertical_speed

    def apply_output(self, output):
        self.log_data("reading", self.currentReading)
        self.log_data("output", output)
        self.elevatorController.update(output)
