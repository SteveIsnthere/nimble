from flightControl.interface.interface import Interface


class RcPlaneInterface(Interface):
    def __init__(self):
        self.current_altitude = self.altitude
        self.last_altitude = 0
        self.current_vs = 0
        self.last_vs = 0

        self.IMU_MAX_READING_FREQUENCY = 100
        self.GPS_MAX_READING_FREQUENCY = 10
        self.BAROMETER_MAX_READING_FREQUENCY = 10

    @property
    def vertical_speed(self):
        self.last_altitude = self.current_altitude
        self.current_altitude = self.altitude
        self.last_vs = self.current_vs
        self.current_vs = (self.current_altitude - self.last_altitude) / self.delta_time
        self.current_vs = (self.last_vs * 29 + self.current_vs) / 30
        return self.current_vs
