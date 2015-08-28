from core_rover.server.subsystems.fieldbus import Fieldbus

bus = Fieldbus('/dev/ttyUSB0', baud=9600, read_timeout=10.0)


class BaseDriver(object):
    def __init__(self, address):
        self.address = address

    def _request(self, command, params=[], respond=True):
        return bus.request(self.address, respond, command, params)
