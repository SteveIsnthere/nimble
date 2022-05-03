import time

from flightControl.compoents.logger import Logger
from flightControl.test.controllerTest import TestInterface, TestController

data_points_needed = 500
interface = TestInterface()
logger = Logger()

test_controller = TestController(interface, logger)

data_points_count = 0
target = 0
while data_points_count < data_points_needed:
    time.sleep(0.0001)
    if data_points_count == round(data_points_needed / 4):
        target = 50
        print("25%")
    elif data_points_count == round(data_points_needed / 2):
        target = 100
        print("50%")
    elif data_points_count == round(3 * data_points_needed / 4):
        target = 25
        print("75%")
    data_points_count += 1
    interface.update()
    test_controller.update(target)


logger.save()
