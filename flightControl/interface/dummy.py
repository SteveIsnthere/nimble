from flightControl.interface.interface import Interface


class DummyInterface(Interface):
    @property
    def roll(self):
        return 0

    @property
    def pitch(self):
        return 0

    @property
    def heading(self):
        return 0

    @property
    def roll_velocity(self):
        return 0

    @property
    def pitch_velocity(self):
        return 0

    @property
    def yaw_velocity(self):
        return 0

    @property
    def altitude(self):
        return 0

    @property
    def temperature(self):
        return 15

    @property
    def horizontal_speed(self):
        return 0

    @property
    def vertical_speed(self):
        return 0

    @property
    def longitude(self):
        return 0

    @property
    def latitude(self):
        return 0

    @property
    def g_force(self):
        return 0

    def set_pitch(self, output):
        pass

    def set_roll(self, output):
        pass

    def set_throttle(self, output):
        pass

    def update(self):
        pass

    def init(self):
        pass
