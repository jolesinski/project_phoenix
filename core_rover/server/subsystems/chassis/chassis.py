__author__ = 'miczyg'

from core_rover.server.subsystems.drivers import BLDCMotor

class Chassis(object):
    def __init__(self):
        self.left_front_motor = BLDCMotor
        self.left_rear_motor = BLDCMotor
        self.right_front_motor = BLDCMotor
        self.right_rear_motor = BLDCMotor


    def drive(self, speed = 0.0, rotation = 0.0):
        pass


    def stop(self):
        pass
