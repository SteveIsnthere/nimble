import time
import enum
from flightControl.highLevelController.altitudeController import AltitudeController
from flightControl.highLevelController.headingController import HeadingController
from flightControl.compoents.logger import Logger
from flightControl.lowLevelControllers.aileronController import AileronController
from flightControl.lowLevelControllers.elevatorController import ElevatorController
from flightControl.lowLevelControllers.throttleController import ThrottleController
from flightControl.midLevelControllers.verticalSpeedController import VerticalSpeedController
from interface.interface import Interface


class FlightController:
    interface = Interface()
    logger = Logger()
    running = True

    mode = 1

    @property
    def main_ap(self):
        return True

    @property
    def alt_hold(self):
        return True

    @property
    def alt_hold(self):
        return True

    def __init__(self):
        self.aileron_controller = AileronController(self.interface, self.logger)
        self.elevator_controller = ElevatorController(self.interface, self.logger)
        self.throttle_controller = ThrottleController(self.interface, self.logger)

        self.altitude_controller = AltitudeController(self.interface, self.logger)
        self.heading_controller = HeadingController(self.interface, self.logger)

        self.vertical_speed_controller = VerticalSpeedController(self.interface, self.logger)

    def start(self):
        while self.running:
            time.sleep(0.01)
            self.altitude_controller.update(2000)
            self.heading_controller.update(100)
            self.throttle_controller.update(170)

    def stop(self):
        self.running = False
        self.logger.save()
