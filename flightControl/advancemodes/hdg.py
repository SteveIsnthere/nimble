from flightControl.compoents.advancemode import AdvanceMode
from flightControl.controllers.highLevelController.headingController import HeadingController


class HDG(AdvanceMode):
    MAX_HEADING = 360
    MIN_HEADING = 0
    target_heading = 180

    def __init__(self, flight_controller):
        super().__init__(flight_controller)
        self.heading_controller = HeadingController(self.interface, self.logger)

    def control(self):
        self.heading_controller.update(self.target_heading)

    def set(self, target_heading) -> bool:
        if self.MIN_HEADING <= target_heading <= self.MAX_HEADING:
            self.target_heading = target_heading
            return True
        else:
            return False
