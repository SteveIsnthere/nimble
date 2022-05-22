from flightControl.flightController import FlightController
from flightControl.interface.ksp import KspInterface
from handler.gui import GUI

interface = KspInterface()
controller = FlightController(interface)
handler = GUI(controller)
handler.start()
