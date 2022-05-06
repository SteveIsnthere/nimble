import signal
import threading

from util.gui import UI


class UtilHandler:

    def __init__(self, controller):
        self.controller = controller

    def start(self):
        UI(self)

    def controller_state(self):
        return self.controller.is_running()

    def switch_on_controller(self):
        if not self.controller_state():
            threading.Thread(target=self.controller.start).start()

    def switch_off_controller(self):
        if self.controller_state():
            self.controller.stop()
