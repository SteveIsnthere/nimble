from flightControl.compoents.advancemode import AdvanceMode
from flightControl.controllers.lowLevelControllers.speedController import SpeedController


class SPD(AdvanceMode):
    target_speed = 0

    def __init__(self, flight_controller):
        super().__init__(flight_controller)
        self.speed_controller = SpeedController(self.interface, self.logger)

    def control(self):
        self.speed_controller.update(self.target_speed)

    def set(self, target_speed) -> bool:
        self.target_speed = target_speed
        return True
