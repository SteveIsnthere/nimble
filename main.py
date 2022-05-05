import threading
from flightControl.flightController import FlightController
from util.eventHandler import EventHandler

controller = FlightController()
utilHandler = EventHandler(controller)
threading.Thread(target=controller.start()).start()
