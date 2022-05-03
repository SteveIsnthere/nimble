from flightControl.flightController import FlightController
from util.util import UtilHandler

controller = FlightController()
utilHandler = UtilHandler(controller)
controller.start()
