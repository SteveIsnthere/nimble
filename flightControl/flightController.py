import time

from flightControl.advancemodes.alt import ALT
from flightControl.advancemodes.app import APP
from flightControl.advancemodes.hdg import HDG
from flightControl.advancemodes.man import MAN
from flightControl.advancemodes.nav import NAV
from flightControl.advancemodes.spd import SPD
from flightControl.advancemodes.toga import TOGA
from flightControl.advancemodes.vs import VS
from flightControl.compoents.logger import Logger


class FlightController:
    def __init__(self, interface):
        self.util_handler = None
        self.control_modes = None
        self.control_modes_index_table = None
        self.interface = interface
        self.logger = Logger()
        self.running = False

    def init(self):
        if self.util_handler is None:
            raise Exception('FlightController no handler assigned')

        self.control_modes = []
        self.control_modes.append(ALT(self))
        self.control_modes.append(VS(self))
        self.control_modes.append(HDG(self))
        self.control_modes.append(SPD(self))
        self.control_modes.append(MAN(self))
        self.control_modes.append(NAV(self))
        self.control_modes.append(APP(self))
        self.control_modes.append(TOGA(self))

        self.control_modes_index_table = {}
        for i in range(len(self.control_modes)):
            name = type(self.control_modes[i]).__name__
            self.control_modes_index_table.update({name: i})

    def is_running(self):
        return self.running

    def set_handler(self, handler):
        self.util_handler = handler

    def start(self):
        self.init()
        self.running = True
        self.push_state_update("running", True)
        try:
            self.control_loop()
        except Exception as e:
            self.stop()
            print(e)

    def control_loop(self):
        while self.running:
            time.sleep(0.01)
            for mode in self.control_modes:
                mode.update()

    def stop(self):
        self.running = False
        self.push_state_update("running", False)
        self.logger.save()

    def toggle_mode(self, name):
        index = self.control_modes_index_table[name]
        self.control_modes[index].toggle()

    def set_mode(self, name, val):
        index = self.control_modes_index_table[name]
        self.control_modes[index].set(val)

    def push_state_update(self, name, state):
        self.util_handler.receive_state_update(name, state)
