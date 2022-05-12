from flightControl.flightController import FlightController
from flightControl.interface.ksp import KSP_Interface
from util.utilHandler import UtilHandler

interface = KSP_Interface()
controller = FlightController(interface)
util_handler = UtilHandler(controller)
util_handler.start()
