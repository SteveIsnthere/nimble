from others.controller import Controller


class TestInterface:
    value = 50
    dv = 0
    controlOutPut = 0

    @property
    def reading(self):
        return self.value

    @property
    def output_effect(self):
        return self.controlOutPut * 1

    def set_output(self, output):
        self.controlOutPut = output

    def update(self):
        self.value = self.value
        # self.dv += np.random.rand() * 0.1
        self.dv += self.controlOutPut
        self.value += self.dv


class TestController(Controller):
    default_min_output = -1
    default_max_output = 1
    default_delta_time = 1

    def __init__(self, interface, logger):
        super().__init__("TestController", interface, logger, self.default_min_output, self.default_max_output)

    def get_current_reading(self):
        return self.interface.reading

    def apply_output(self, output):
        self.log_data("reading", self.currentReading)
        self.log_data("delta_time", self.delta_time)
        self.log_data("output", output)
        self.interface.set_output(output)
