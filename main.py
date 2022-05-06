from flightControl.flightController import FlightController
from util.utilHandler import UtilHandler

controller = FlightController()
util_handler = UtilHandler(controller)
util_handler.start()
