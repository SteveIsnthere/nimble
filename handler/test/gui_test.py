from flightControl.flightController import FlightController
from flightControl.interface.dummy import DummyInterface
from handler.gui import GUI

interface = DummyInterface()
controller = FlightController(interface)
handler = GUI(controller)
handler.start()