import time
from flightControl.highLevelController.altitudeController import AltitudeController
from flightControl.highLevelController.headingController import HeadingController
from flightControl.compoents.logger import Logger
from flightControl.lowLevelControllers.throttleController import ThrottleController
from interface.interface import Interface


class FlightController:
    interface = Interface()
    logger = Logger()
    running = True

    def __init__(self):
        self.controller_1 = AltitudeController(self.interface, self.logger)  # ElevatorController(interface, logger)
        self.controller_2 = HeadingController(self.interface, self.logger)  # AileronController(interface, logger)
        self.throttle_controller = ThrottleController(self.interface, self.logger)

    def start(self):
        while self.running:
            time.sleep(0.01)
            self.controller_1.update(3000)
            self.controller_2.update(100)
            self.throttle_controller.update(150)

    def stop(self):
        self.running = False
        self.logger.save()
