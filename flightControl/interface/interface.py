class Interface:
    stall = False
    g_overload = False
    home_point_position = None  # [0, 0]
    home_point_alt = None  # 0

    @property
    def roll(self):
        raise Exception('Interface not implemented')

    @property
    def pitch(self):
        raise Exception('Interface not implemented')

    @property
    def heading(self):
        raise Exception('Interface not implemented')

    @property
    def heading_gps(self):
        raise Exception('Interface not implemented')

    @property
    def roll_velocity(self):
        raise Exception('Interface not implemented')

    @property
    def pitch_velocity(self):
        raise Exception('Interface not implemented')

    @property
    def turn_velocity(self):
        raise Exception('Interface not implemented')

    @property
    def altitude(self):
        raise Exception('Interface not implemented')

    @property
    def temperature(self):
        raise Exception('Interface not implemented')

    @property
    def horizontal_speed(self):
        raise Exception('Interface not implemented')

    @property
    def vertical_speed(self):
        raise Exception('Interface not implemented')

    @property
    def position(self):
        raise Exception('Interface not implemented')

    @property
    def g_force(self):
        raise Exception('Interface not implemented')

    def set_elevator(self, output):
        raise Exception('Interface not implemented')

    def set_aileron(self, output):
        raise Exception('Interface not implemented')

    def set_throttle(self, output):
        raise Exception('Interface not implemented')

    def update(self):
        raise Exception('Interface not implemented')

    def init(self):
        raise Exception('Interface not implemented')
