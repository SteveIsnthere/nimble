import signal


class UtilHandler:

    def __init__(self, controller):
        self.controller = controller

        # noinspection PyUnusedLocal
        def signal_handler(s, frame):
            self.controller.stop()

        signal.signal(signal.SIGINT, signal_handler)
