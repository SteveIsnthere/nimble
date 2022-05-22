from others.controller import Controller
from flightControl.controllers.lowLevelControllers.pitchController import PitchController


class LevelChangeController(Controller):
    # feed:speed out:pitch
    default_min_output = -25
    default_max_output = 35

    def __init__(self, interface, logger):
        super().__init__("LevelChangeController", interface, logger, self.default_min_output,
                         self.default_max_output)
        self.elevatorController = PitchController(interface, logger)
        self.pid.tunings = (5, 0.3, 0.3)

    def get_current_reading(self):
        return self.interface.horizontal_speed

    def apply_output(self, output):
        self.log_data("reading", self.currentReading)
        self.log_data("output", output)
        self.elevatorController.update(output)
