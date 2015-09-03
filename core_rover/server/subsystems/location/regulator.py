import math
from math import cos
from math import sin
import thread
import time
from server.subsystems.chassis.chassis import Chassis
from server.subsystems.location.basegps import GpsModule

class Regulator(object):
    def __init__(self):
        self.gps = GpsModule
        self.driver = Chassis
        self.is_autonomous = False
        self.destination = [0.0, 0,0]
        self.position = [0.0, 0.0]
        self.rem_distance = 0

    def run_auto(self, latitude, longitude, speed):
        thread.start_new_thread(self.control_drive, (latitude, longitude, speed) ) #???

    def control_drive(self, latitude, longitude, speed = 1.0):
        self.is_autonomous = True
        self.destination = [latitude, longitude]

        self.position = self.gps.getGPS()
        self.rem_distance = self.distance_to(position, self.destination)

        while self.is_autonomous and self.rem_distance > 5:
            expected_course = self.course_to(self.destination)
            current_course = self.gps.getOGI()[1]
            deviation = self.calculate_steering(current_course, expected_course)
            self.driver.drive(speed=speed, rotation=deviation)
            time.sleep(10) #???
            self.rem_distance = self.distance_to(self.position, self.destination)

        return 0

    def calculate_steering(self, curr_course, expected_course): #expected in radians
        diff = expected_course - curr_course
        if diff < -math.pi:
            diff = diff + 2 * math.pi

        deviation = diff / math.pi
        if diff > math.pi / 2 or diff < -math.pi / 2:
            deviation = math.copysign(1, diff)

        return deviation

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

    def course_to(self, destination):
        position = self.position = self.gps.getGPS()
        diff_long = math.radians( position[1] - destination[1] )
        pos_lati = math.radians(position[0])
        dest_lati = math.radians(destination[0])

        course_dump1 = sin(diff_long) - cos(dest_lati)
        course_dump2 = sin(pos_lati) * cos(dest_lati) * cos(diff_long)
        course_dump2 = cos(pos_lati) * sin(dest_lati) - course_dump2

        course = math.atan2(course_dump1, course_dump2)

        if course < 0:
            course += 2 * math.pi

        return course

    def stop_automatic_drive(self):
        self.is_autonomous = False
