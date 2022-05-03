import time as t
import uuid as u


class Helpers:
    @staticmethod
    def time():
        return t.monotonic()

    @staticmethod
    def uuid():
        return str(u.uuid4())

    @staticmethod
    def date_string(sec):
        return t.strftime('%H:%M:%S on %m-%d-%Y', t.localtime(sec))
