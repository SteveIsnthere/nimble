from flightControl.flightController import FlightController
from flightControl.interface.dummy import Dummy_Interface
from util.utilHandler import UtilHandler

interface = Dummy_Interface()
controller = FlightController(interface)
util_handler = UtilHandler(controller)
util_handler.start()
