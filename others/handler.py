import threading
from abc import abstractmethod


class Handler:
    def __init__(self, controller):
        self.controller = controller
        self.controller.set_handler(self)

    @abstractmethod
    def start(self):
        pass

    def is_controller_on(self):
        return self.controller.is_running()

    def switch_on_controller(self):
        if not self.is_controller_on():
            threading.Thread(target=self.controller.start).start()

    def switch_off_controller(self):
        if self.is_controller_on():
            self.controller.stop()

    @abstractmethod
    def receive_state_update(self, name, state):
        if name == "ALT":
            pass
        elif name == "VS":
            pass
        elif name == "HDG":
            pass
        elif name == "SPD":
            pass
        elif name == "MAN":
            pass
        elif name == "NAV":
            pass
        elif name == "APP":
            pass
        elif name == "TOGA":
            pass
        elif name == "running":
            pass

    def toggle_mode(self, name):
        self.controller.toggle_mode(name)

    def set_mode(self, name, val):
        self.controller.set_mode(name, val)
