from math import pi

import krpc


class KSP:
    def __init__(self):
        self.conn = krpc.connect(name='sim')
        self.vessel = self.conn.space_center.active_vessel
        self.ref = self.vessel.orbit.body.reference_frame
        self.flight = self.vessel.flight(self.ref)

    @property
    def roll(self):
        return self.vessel.flight().roll

    @property
    def pitch(self):
        return self.vessel.flight().pitch

    @property
    def heading(self):
        return self.vessel.flight().heading

    @property
    def roll_velocity(self):
        return -self.vessel.angular_velocity(self.vessel.orbit.body.non_rotating_reference_frame)[0] / pi * 180

    @property
    def pitch_velocity(self):
        return self.vessel.angular_velocity(self.vessel.orbit.body.non_rotating_reference_frame)[1] / pi * 180

    @property
    def yaw_velocity(self):
        return self.vessel.angular_velocity(self.vessel.orbit.body.non_rotating_reference_frame)[2] / pi * 180

    @property
    def altitude(self):
        return self.vessel.flight().mean_altitude

    @property
    def temperature(self):
        return 15

    @property
    def horizontal_speed(self):
        return self.flight.horizontal_speed

    @property
    def vertical_speed(self):
        return self.flight.vertical_speed

    @property
    def longitude(self):
        return self.vessel.flight().longitude

    @property
    def latitude(self):
        return self.vessel.flight().latitude

    @property
    def g_force(self):
        return self.vessel.flight().g_force

    def set_pitch(self, output):
        self.vessel.control.pitch = output

    def set_roll(self, output):
        self.vessel.control.roll = output

    def set_throttle(self, output):
        self.vessel.control.throttle = output
