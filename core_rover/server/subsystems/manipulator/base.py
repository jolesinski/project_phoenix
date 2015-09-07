from subsystems.drivers import StepperMotor, ServoMotor


class Gripper(StepperMotor):
    def open(self):
        #Set gripper motor max open
        raise NotImplementedError

    def grab(self):
        #Set gripper motor min open
        raise NotImplementedError


class Manipulator(object):
    def __init__(self):
        self.joints = [StepperMotor(address=101),
                       StepperMotor(address=102),
                       StepperMotor(address=103),
                       StepperMotor(address=104),
                       ServoMotor(address=105),
                       StepperMotor(address=105)]
        self.gripper = Gripper(address=106);

    def set_joint_angles(self, angles):
        for i in range(len(self.joints)):
            self.joints[i].set_angle(angles[i])

    def set_effector_position(self, x, y, z):
        #Calculate inverse kinematics with kinematics.py
        raise NotImplementedError

