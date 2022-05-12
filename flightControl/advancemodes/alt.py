from flightControl.compoents.advancemode import AdvanceMode
from flightControl.controllers.highLevelController.altitudeController import AltitudeController


class ALT(AdvanceMode):
    MAX_ALT = 50000
    MIN_ALT = -200
    target_altitude = 1000

    def __init__(self, flight_controller):
        super().__init__(flight_controller)
        self.altitude_controller = AltitudeController(self.interface, self.logger)

    def control(self):
        self.altitude_controller.update(self.target_altitude)

    def toggle_logic(self):
        if not self.toggled_on:
            self.altitude_controller = AltitudeController(self.interface, self.logger)
            for mode in self.flight_controller.control_modes:
                if type(mode).__name__ in ["NAV", "APP", "TOGA", "VS"] and mode.is_on():
                    mode.toggle()
        self.toggled_on = not self.toggled_on

    def set(self, target_altitude) -> bool:
        if self.MIN_ALT <= target_altitude <= self.MAX_ALT:
            self.target_altitude = target_altitude
            return True
        else:
            return False
