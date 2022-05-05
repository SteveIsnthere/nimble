import signal

from util.gui import UI


class UtilHandler:

    def __init__(self, controller):
        self.controller = controller

        # noinspection PyUnusedLocal
        def signal_handler(s, frame):
            print("signal.SIGINT handled")
            self.stop()

        signal.signal(signal.SIGINT, signal_handler)

    def start(self):
        UI(self)

    def stop(self):
        print("clicked")
        self.controller.stop()
