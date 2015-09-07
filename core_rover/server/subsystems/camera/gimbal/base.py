from subsystems.drivers import ServoMotor


class Gimbal(object):
    def __init__(self):
        self.servo_x = ServoMotor(address=103)
        self.servo_z = ServoMotor(address=104)

    def set_orientation(self, angle_x, angle_z):
        self.servo_x.set_angle(angle_x)
        self.servo_z.set_angle(angle_z)