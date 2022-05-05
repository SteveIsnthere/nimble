from flightControl.compoents.advancemode import AdvanceMode
from flightControl.controllers.midLevelControllers.verticalSpeedController import VerticalSpeedController


class VS(AdvanceMode):
    MAX_VS = 50
    MIN_VS = -50
    target_vs = 1000

    def __init__(self, flight_controller):
        super().__init__(flight_controller)
        self.vertical_speed_controller = VerticalSpeedController(self.interface, self.logger)

    def control(self):
        self.vertical_speed_controller.update(self.target_vs)

    def set(self, target_vs) -> bool:
        if self.MIN_VS <= target_vs <= self.MAX_VS:
            self.target_vs = target_vs
            return True
        else:
            return False
