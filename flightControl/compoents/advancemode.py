class AdvanceMode:
    def __init__(self, flight_controller):
        self.interface = flight_controller.interface
        self.logger = flight_controller.logger
        self.toggled_on = False

    def update(self):
        if not self.toggled_on:
            return
        self.control()

    def toggle(self) -> bool:
        self.toggled_on = not self.toggled_on
        return True

    def control(self):
        raise Exception('please override this method')

    def set(self, val) -> bool:
        return True


