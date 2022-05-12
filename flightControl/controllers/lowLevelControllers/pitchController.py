from flightControl.compoents.controller import Controller


class PitchController(Controller):
    default_elevator_min_output = -1
    default_elevator_max_output = 1

    def __init__(self, interface, logger):
        super().__init__("PitchController", interface, logger, self.default_elevator_min_output,
                         self.default_elevator_max_output)
        self.pid.tunings = (0.03, 0.005, 0.01)

    @property
    def current_reading_change_rate(self):
        return self.interface.pitch_velocity

    def get_current_reading(self):
        return self.interface.pitch

    def apply_output(self, output):
        self.log_data("reading", self.currentReading)
        self.log_data("output", output)
        self.interface.set_elevator(output)
        return
