from flightControl.compoents.controller import Controller
from flightControl.controllers.midLevelControllers.verticalSpeedController import VerticalSpeedController


class AltitudeController(Controller):
    # feed:alt out:vSpeed
    default_min_output = -50
    default_max_output = 50

    def __init__(self, interface, logger):
        super().__init__("AltitudeController", interface, logger, self.default_min_output,
                         self.default_max_output)
        self.verticalSpeedController = VerticalSpeedController(interface, logger)
        self.pid.tunings = (0.25, 0, 0)

    def get_current_reading(self):
        return self.interface.altitude

    def apply_output(self, output):
        self.log_data("reading", self.currentReading)
        self.log_data("output", output)
        self.verticalSpeedController.update(output)
