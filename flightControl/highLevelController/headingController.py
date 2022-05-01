from flightControl.compoents.controller import Controller
from flightControl.midLevelControllers.turingSpeedController import TurningSpeedController


class HeadingController(Controller):
    # feed:heading out:turningSpeed
    default_min_output = -30
    default_max_output = 30

    def __init__(self, interface, logger):
        super().__init__("HeadingController", interface, logger, self.default_min_output,
                         self.default_max_output)
        self.turningSpeedController = TurningSpeedController(interface, logger)
        self.pid.tunings = (0.4, 0, 0)

    def get_current_reading(self):
        return self.interface.heading

    def apply_output(self, output):
        self.log_data("reading", self.currentReading)
        self.log_data("output", output)
        self.turningSpeedController.update(output)
