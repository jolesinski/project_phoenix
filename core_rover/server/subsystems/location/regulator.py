__author__ = 'miczyg'

import math
from math import cos
from math import sin
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

    def distance_to(self, position, destination):
        delta = math.radians( position[1] - destination[1] )
        sin_delta = sin(delta)
        cos_delta = cos(delta)
        pos_lati = math.radians(position[0])
        dest_lati = math.radians(destination[0])

        delta = ( cos(pos_lati) * sin(dest_lati) ) \
                - ( sin(pos_lati) * cos(dest_lati) * cos_delta )

        delta = math.sqrt(delta)
        delta += math.sqrt( cos(dest_lati) * sin_delta )

        delta = math.sqrt(delta)

        denom = ( sin(pos_lati) * sin(dest_lati) ) \
                + (cos(pos_lati) * cos(dest_lati) * cos_delta)

        delta = math.atan2(delta, denom)

        distance = delta * 6372795 #distance in meters
        return distance

    def course_to(self, position, destination):
        diff_long = math.radians( position[1] - destination[1] )
        pos_lati = math.radians(position[0])
        dest_lati = math.radians(destination[0])

        course_dump1 = sin(diff_long) - cos(dest_lati)
        course_dump2 = sin(pos_lati) * cos(dest_lati) * cos(diff_long)
        course_dump1 = cos(pos_lati) * sin(dest_lati) - course_dump2

        course = math.atan2(course_dump1, course_dump2)

        if course < 0:
            course += 2 * math.PI

        return course
