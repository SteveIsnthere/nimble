import time

from flightControl.advancemodes.alt import ALT
from flightControl.advancemodes.app import APP
from flightControl.advancemodes.hdg import HDG
from flightControl.advancemodes.nav import NAV
from flightControl.advancemodes.toga import TOGA
from flightControl.advancemodes.vs import VS
from flightControl.compoents.logger import Logger
from interface.interface import Interface


class FlightController:
    interface = Interface()
    logger = Logger()
    running = True

    def __init__(self):
        self.ALT = ALT(self)
        self.VS = VS(self)
        self.HDG = HDG(self)
        self.NAV = NAV(self)
        self.APP = APP(self)
        self.TOGA = TOGA(self)

    def start(self):
        while self.running:
            time.sleep(0.01)
            self.ALT.update()
            self.VS.update()
            self.HDG.update()
            self.NAV.update()
            self.APP.update()
            self.TOGA.update()

    def stop(self):
        self.running = False
        self.logger.save()
