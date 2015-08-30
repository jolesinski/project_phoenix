__author__ = 'miczyg'

import math
from server.subsystems.chassis.chassis import Chassis
from server.subsystems.location.basegps import GpsModule

class Regulator(object):
    def __init__(self):
        self.gps = GpsModule
        self.driver = Chassis

        self.destination = [0.0, 0,0]

    #TODO: steering alg to control drive conversion
    def control_drive(self):
        pass

    def set_destination(self, latitude, longitude):
        self.destination = [latitude, longitude]

    #TODO: sterring algorithm
    def calculate_steering(self):
        current_position = self.gps.getGPS()
        lat_diff = self.destination[0] - current_position[0]
        long_diff = self.destination[1] - current_position[1]
        distance = math.hypot(lat_diff, long_diff)
        pass
