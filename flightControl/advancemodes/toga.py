from flightControl.compoents.advancemode import AdvanceMode
from flightControl.controllers.lowLevelControllers.rollController import RollController
from flightControl.controllers.lowLevelControllers.pitchController import PitchController
from flightControl.controllers.lowLevelControllers.speedController import SpeedController


class TOGA(AdvanceMode):
    TOGA_PITCH = 15
    TOGA_THRUST = 0.95

    def __init__(self, flight_controller):
        super().__init__(flight_controller)
        self.toggled_on = True
        self.roll_controller = RollController(self.interface, self.logger)
        self.pitch_controller = PitchController(self.interface, self.logger)

    def control(self):
        self.roll_controller.update(0)
        self.pitch_controller.update(self.TOGA_PITCH)
        self.interface.set_throttle(self.TOGA_THRUST)
