from flightControl.compoents.advancemode import AdvanceMode


class MAN(AdvanceMode):

    def __init__(self, flight_controller):
        super().__init__(flight_controller)

    def control(self):
        return
