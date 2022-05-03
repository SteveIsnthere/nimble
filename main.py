import signal

running = True
controller = FlightController()
controller
def signal_handler(s, frame):
    global running
    running = False


signal.signal(signal.SIGINT, signal_handler)
