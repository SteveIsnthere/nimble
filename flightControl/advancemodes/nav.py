from flightControl.compoents.advancemode import AdvanceMode


class NAV(AdvanceMode):
    way_points = []

    def __init__(self, flight_controller):
        super().__init__(flight_controller)

    def control(self):
        return
