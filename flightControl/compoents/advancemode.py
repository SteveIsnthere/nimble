class AdvanceMode:
    def __init__(self, flight_controller):
        self.flight_controller = flight_controller
        self.interface = flight_controller.interface
        self.logger = flight_controller.logger
        self.toggled_on = False
        self.state_update()

    def update(self):
        if not self.toggled_on:
            return
        self.control()

    def toggle(self):
        self.toggle_logic()
        self.state_update()

    def toggle_logic(self):
        self.toggled_on = not self.toggled_on

    def turn_off_other_modes_when_turn_on(self):
        if not self.is_on():
            for mode in self.flight_controller.control_modes:
                if mode != self and mode.is_on():
                    mode.toggle()

    def state_update(self):
        self.flight_controller.push_state_update(type(self).__name__, self.is_on())

    def is_on(self):
        return self.toggled_on

    def control(self):
        raise Exception('please override this method')

    def set(self, val) -> bool:
        return True
