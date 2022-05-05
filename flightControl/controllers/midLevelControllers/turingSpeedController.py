from flightControl.compoents.controller import Controller
from flightControl.controllers.lowLevelControllers.aileronController import AileronController


class TurningSpeedController(Controller):
    # feed:TurningSpeed out:roll
    default_min_output = -30
    default_max_output = 30

    def __init__(self, interface, logger):
        super().__init__("TurningSpeedController", interface, logger, self.default_min_output,
                         self.default_max_output)
        self.aileronController = AileronController(interface, logger)
        self.current_heading = self.interface.heading
        self.last_heading = 0
        self.current_turning_speed = 0
        self.last_turning_speed = 0
        self.pid.tunings = (7, 0, 0.05)

    def get_current_reading(self):
        self.last_heading = self.current_heading
        self.current_heading = self.interface.heading
        self.last_turning_speed = self.current_turning_speed
        self.current_turning_speed = (self.current_heading - self.last_heading) / self.delta_time
        self.current_turning_speed = (self.last_turning_speed * 14 + self.current_turning_speed) / 15
        return self.current_turning_speed

    def apply_output(self, output):
        self.log_data("reading", self.current_turning_speed)
        self.log_data("output", output)
        self.aileronController.update(output)
