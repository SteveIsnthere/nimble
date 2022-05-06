from flightControl.compoents.controller import Controller


class RollController(Controller):
    default_aileron_min_output = -1
    default_aileron_max_output = 1

    def __init__(self, interface, logger):
        super().__init__("RollController", interface, logger, self.default_aileron_min_output,
                         self.default_aileron_max_output)
        self.pid.tunings = (0.0055, 0.0001, 0.0005)

    @property
    def current_reading_change_rate(self):
        return self.interface.roll_velocity

    def get_current_reading(self):
        return self.interface.roll

    def apply_output(self, output):
        self.log_data("reading", self.currentReading)
        self.log_data("output", output)
        self.interface.set_roll(output)
        return
