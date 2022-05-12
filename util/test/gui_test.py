from flightControl.flightController import FlightController
from flightControl.interface.dummy import DummyInterface
from util.utilHandler import UtilHandler

interface = DummyInterface()
controller = FlightController(interface)
util_handler = UtilHandler(controller)
util_handler.start()
