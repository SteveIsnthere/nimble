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
from flightControl.interface.interface import Interface


class FlightController:

    def __init__(self):
        self.control_modes = None
        self.control_modes_name_list = None
        self.interface = Interface()
        self.logger = Logger()
        self.running = False

    def init(self):
        self.control_modes = []
        self.control_modes.append(ALT(self))
        self.control_modes.append(VS(self))
        self.control_modes.append(HDG(self))
        self.control_modes.append(SPD(self))
        self.control_modes.append(MAN(self))
        self.control_modes.append(NAV(self))
        self.control_modes.append(APP(self))
        self.control_modes.append(TOGA(self))

        self.control_modes_name_list = []
        for mode in self.control_modes:
            self.control_modes_name_list.append(type(mode).__name__)

    def is_running(self):
        return self.running

    def start(self):
        self.init()
        self.running = True
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
        self.logger.save()

    def mode_is_on(self, name):
        for mode in self.control_modes:
            if type(mode).__name__ == name:
                return mode.is_on()
        return False

    def toggle_mode(self, name):
        for mode in self.control_modes:
            if type(mode).__name__ == name:
                successful = mode.toggle()
                return successful
        return False
