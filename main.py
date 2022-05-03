from flightControl.flightController import FlightController
from util.eventHandler import EventHandler

controller = FlightController()
utilHandler = EventHandler(controller)
controller.start()
