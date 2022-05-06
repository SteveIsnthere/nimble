from flightControl.compoents.controller import Controller


class SpeedController(Controller):
    default_throttle_min_output = 0
    default_throttle_max_output = 1

    def __init__(self, interface, logger):
        super().__init__("SpeedController", interface, logger, self.default_throttle_min_output,
                         self.default_throttle_max_output)
        self.pid.tunings = (0.03, 0.001, 0.005)

    def get_current_reading(self):
        return self.interface.horizontal_speed

    def apply_output(self, output):
        self.log_data("reading", self.currentReading)
        self.log_data("output", output)
        self.interface.set_throttle(output)
        return
