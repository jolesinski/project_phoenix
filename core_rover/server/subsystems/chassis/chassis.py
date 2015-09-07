import math
from subsystems.drivers import DrillerMotor


class Chassis(object):
    def __init__(self, left_side_address=76, right_side_address=82):
        self.left_front_motor = DrillerMotor(address=left_side_address, driller_num=0)
        self.left_central_motor = DrillerMotor(address=left_side_address, driller_num=1)
        self.left_rear_motor = DrillerMotor(address=left_side_address, driller_num=2)

        self.right_front_motor = DrillerMotor(address=right_side_address, driller_num=0)
        self.right_central_motor = DrillerMotor(address=right_side_address, driller_num=1)
        self.right_rear_motor = DrillerMotor(address=right_side_address, driller_num=2)

        self.sensivity = 0.5

        self.left_power = 0
        self.left_direction = 0
        self.right_power = 0
        self.right_direction = 0

    def drive(self, speed=0.0, rotation=0.0):
        if rotation < 0:
            rotation = math.fabs(rotation)
            ratio = self.calculate_ratio(rotation)
            left_speed = speed / ratio
            right_speed = speed

            self.calculate_steering(left_speed, right_speed)
            self.steer_front()
            self.steer_central()
            self.steer_rear()

        elif rotation > 0:
            ratio = self.calculate_ratio(rotation)
            left_speed = speed
            right_speed = speed / ratio

            self.calculate_steering(left_speed, right_speed)
            self.steer_front()
            self.steer_central()
            self.steer_rear()

        else:
            self.calculate_steering(speed, speed)
            self.steer_rear()
            self.steer_central()
            self.steer_front()

    def stop(self):
        self.left_front_motor.stop()
        self.right_front_motor.stop()
        self.left_central_motor.stop()
        self.right_central_motor.stop()
        self.left_rear_motor.stop()
        self.right_rear_motor.stop()

    def calculate_ratio(self, curve):
        ratio = math.log(curve)
        ratio = (ratio - self.sensivity) / (ratio + self.sensivity)
        if ratio == 0:
            ratio = .0000000001

        return ratio

    def calculate_steering(self, left_speed, right_speed):
        self.left_direction = int(math.copysign(1, left_speed))
        self.right_direction = int(math.copysign(1, right_speed))

        self.left_power = math.fabs(left_speed)
        self.left_power = int(self.left_power * 255)

        self.right_power = math.fabs(right_speed)
        self.right_power = int(self.right_power * 255)

    def steer_front(self):

        self.left_front_motor.set_direction(self.left_direction)
        self.right_front_motor.set_direction(self.right_direction)

        self.left_front_motor.set_power(self.left_power)
        self.right_front_motor.set_power(self.right_power)

    def steer_central(self):
        self.left_central_motor.set_direction(self.left_direction)
        self.right_central_motor.set_direction(self.right_direction)

        self.left_central_motor.set_power(self.left_power)
        self.right_central_motor.set_power(self.right_power)

    def steer_rear(self):
        self.left_rear_motor.set_direction(self.left_direction)
        self.right_rear_motor.set_direction(self.right_direction)

        self.left_rear_motor.set_power(self.left_power)
        self.right_rear_motor.set_power(self.right_power)
