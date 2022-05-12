from flightControl.compoents.advancemode import AdvanceMode
from flightControl.controllers.midLevelControllers.verticalSpeedController import VerticalSpeedController


class VS(AdvanceMode):
    MAX_VS = 100
    MIN_VS = -100
    target_vs = 0

    def __init__(self, flight_controller):
        super().__init__(flight_controller)
        self.vertical_speed_controller = VerticalSpeedController(self.interface, self.logger)

    def control(self):
        self.vertical_speed_controller.update(self.target_vs)

    def toggle_logic(self):
        if not self.toggled_on:
            self.vertical_speed_controller = VerticalSpeedController(self.interface, self.logger)
            for mode in self.flight_controller.control_modes:
                if type(mode).__name__ in ["NAV", "APP", "TOGA", "ALT"] and mode.is_on():
                    mode.toggle()
        self.toggled_on = not self.toggled_on

    def set(self, target_vs) -> bool:
        if self.MIN_VS <= target_vs <= self.MAX_VS:
            self.target_vs = target_vs
            return True
        else:
            return False
