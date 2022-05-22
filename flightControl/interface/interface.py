from abc import abstractmethod


class Interface:
    DEFAULT_FETCH_DATA_FREQUENCY = 100
    IMU_FETCH_DATA_FREQUENCY = DEFAULT_FETCH_DATA_FREQUENCY
    GPS_FETCH_DATA_FREQUENCY = DEFAULT_FETCH_DATA_FREQUENCY
    BAROMETER_FETCH_DATA_FREQUENCY = DEFAULT_FETCH_DATA_FREQUENCY

    stalling = False
    g_overloading = False
    home_point_pos = None  # [0, 0]
    home_point_alt = None  # 0

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @property
    @abstractmethod
    def roll(self):
        pass

    @property
    @abstractmethod
    def pitch(self):
        pass

    @property
    @abstractmethod
    def heading(self):
        pass

    @property
    @abstractmethod
    def heading_gps(self):
        pass

    @property
    @abstractmethod
    def roll_velocity(self):
        pass

    @property
    @abstractmethod
    def pitch_velocity(self):
        pass

    @property
    @abstractmethod
    def turn_velocity(self):
        pass

    @property
    @abstractmethod
    def altitude(self):
        pass

    @property
    @abstractmethod
    def temperature(self):
        pass

    @property
    @abstractmethod
    def horizontal_speed(self):
        pass

    @property
    @abstractmethod
    def vertical_speed(self):
        pass

    @property
    @abstractmethod
    def position(self):
        pass

    @property
    @abstractmethod
    def g_load(self):
        pass

    @abstractmethod
    def set_elevator(self, output):
        pass

    @abstractmethod
    def set_aileron(self, output):
        pass

    @abstractmethod
    def set_throttle(self, output):
        pass
