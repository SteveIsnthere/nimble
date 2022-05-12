import threading

from util.gui import UI


class UtilHandler:

    def __init__(self, controller):
        self.controller = controller
        self.controller.set_handler(self)
        self.command_handler = UI(self)

    def start(self):
        self.command_handler.start()

    def is_controller_on(self):
        return self.controller.is_running()

    def switch_on_controller(self):
        if not self.is_controller_on():
            threading.Thread(target=self.controller.start).start()

    def switch_off_controller(self):
        if self.is_controller_on():
            self.controller.stop()

    def receive_state_update(self, name, state):
        self.command_handler.receive_update(name, state)

    def toggle_mode(self, name):
        self.controller.toggle_mode(name)

    def set_mode(self, name, val):
        self.controller.set_mode(name, val)
