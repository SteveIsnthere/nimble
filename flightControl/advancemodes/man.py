from others.advancemode import AdvanceMode


class MAN(AdvanceMode):

    def __init__(self, flight_controller):
        super().__init__(flight_controller)

    def control(self):
        return

    def toggle_logic(self):
        self.turn_off_other_modes_when_turn_on()
        self.toggled_on = not self.toggled_on
