__author__ =

import math
from core_rover.server.subsystems.drivers import DrillerMotor



class Chassis(object):
    def __init__(self, left_side_address = 76, right_side_address = 82):
        self.left_front_motor = DrillerMotor( address = left_side_address, driller_num=0 )
        self.left_central_motor = DrillerMotor ( address=left_side_address, driller_num=1 )
        self.left_rear_motor = DrillerMotor( address = left_side_address, driller_num=2 )

        self.right_front_motor = DrillerMotor (address=right_side_address, driller_num=0)
        self.right_central_motor = DrillerMotor(address=right_side_address, driller_num=1)
        self.right_rear_motor = DrillerMotor(address=right_side_address, driller_num=2)
        self.drive()
        self.sensivity = 0.5

    def drive(self, speed = 0.0, rotation = 0.0):
        if rotation < 0:
            rotation = math.fabs(rotation)
            self.turn_left(speed, rotation)

        elif rotation > 0:
            self.turn_right(speed, rotation)

        else:
            self.steer_left_side( speed )
            self.steer_right_side( speed )


    def stop(self):
        pass


    def turn_right(self, speed, curve):
        ratio = math.log( curve )
        ratio = ( ratio - self.sensivity ) / ( ratio + self.sensivity )
        if ratio == 0:
            ratio = .0000000001

        left_speed = speed
        right_speed = speed / ratio

        self.steer_left_side( left_speed )
        self.steer_right_side( right_speed )


    def turn_left(self, speed, curve):
        ratio = math.log( curve )
        ratio = ( ratio - self.sensivity ) / ( ratio + self.sensivity )
        if ratio == 0:
            ratio = .0000000001

        left_speed = speed / ratio
        right_speed = speed

        self.steer_left_side( left_speed )
        self.steer_right_side( right_speed )

    #TODO: probably needs steering not side but front / central / rear
    def steer_left_side(self, speed):
        direction = int ( math.copysign(1, speed) )
        power = math.fabs(speed)
        power = int ( power * 255 )

        self.left_front_motor.set_direction( direction )
        self.left_central_motor.set_direction( direction )
        self.left_rear_motor.set_direction( direction )

        self.left_front_motor.set_power( power )
        self.left_central_motor.set_power( power )
        self.left_rear_motor.set_power( power )

    def steer_right_side(self, speed):
        direction = int ( math.copysign(1, speed) )
        power = math.fabs(speed)
        power = int ( power * 255 )

        self.right_front_motor.set_direction( direction )
        self.right_central_motor.set_direction( direction )
        self.right_rear_motor.set_direction( direction )

        self.right_front_motor.set_power( power )
        self.right_central_motor.set_power( power )
        self.right_rear_motor.set_power( power )