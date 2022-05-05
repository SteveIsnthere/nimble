from flightControl.compoents.advancemode import AdvanceMode
from flightControl.controllers.lowLevelControllers.aileronController import AileronController
from flightControl.controllers.lowLevelControllers.elevatorController import ElevatorController
from flightControl.controllers.lowLevelControllers.throttleController import ThrottleController


class TOGA(AdvanceMode):
    TOGA_PITCH = 15
    TOGA_THRUST = 0.95

    def __init__(self, flight_controller):
        super().__init__(flight_controller)
        self.toggled_on = True
        self.aileron_controller = AileronController(self.interface, self.logger)
        self.elevator_controller = ElevatorController(self.interface, self.logger)

    def control(self):
        self.aileron_controller.update(0)
        self.elevator_controller.update(self.TOGA_PITCH)
        self.interface.set_throttle(self.TOGA_THRUST)
