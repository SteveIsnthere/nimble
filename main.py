import signal
import time

from flightControl.highLevelController.altitudeController import AltitudeController
from flightControl.highLevelController.headingController import HeadingController
from flightControl.compoents.logger import Logger
from flightControl.lowLevelControllers.throttleController import ThrottleController
from interface.interface import Interface

interface = Interface()
logger = Logger()

controller_1 = AltitudeController(interface, logger)
controller_2 = HeadingController(interface, logger)
# controller_1 = ElevatorController(interface, logger)
# controller_2 = AileronController(interface, logger)
throttle_controller = ThrottleController(interface, logger)

running = True


def signal_handler(s, frame):
    global running
    running = False


signal.signal(signal.SIGINT, signal_handler)

while running:
    time.sleep(0.01)
    controller_1.update(3000)
    controller_2.update(100)
    throttle_controller.update(150)

logger.save()
