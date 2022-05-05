import threading
from flightControl.flightController import FlightController
from util.utilHandler import UtilHandler

controller = FlightController()
util_handler = UtilHandler(controller)
threading.Thread(target=controller.start).start()
util_handler.start()
