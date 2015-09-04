from core_rover.server.subsystems.drivers import StepperMotor, ServoMotor


class Gripper(StepperMotor): #not now
    def open(self):
        #Set gripper motor min open
        raise NotImplementedError

    def grab(self):
        #Set gripper motor min open
        raise NotImplementedError


class Manipulator(object):
    def __init__(self): #remember to change addresses
        self.joints = [StepperMotor(address=101), #left/right
                       StepperMotor(address=102), #up1/down1
                       StepperMotor(address=103), #up2/down2
                       StepperMotor(address=104), #rotate gripper
                       ServoMotor(address=105), #catch/open?
                       StepperMotor(address=105)] #catch/open?
        self.gripper = Gripper(address=106) #???

    def set_joint_angles(self, angles):
        for i in range(len(self.joints)):
            self.joints[i].set_angle(angles[i])

    def set_effector_position(self, x, y, z): #not now
        #Calculate inverse kinematics with kinematics.py
        raise NotImplementedError

    def set_joint_speed(self, speeds):
        for i in range(len(self.joints)):
            if isinstance(self.joints[i], StepperMotor):
                self.joints[i].set_speed(angles[i])

    def manipulate_joint(self, action, angle):
        if action == 'RIGHT1' or action == 'LEFT1' #rotates manipulator
            joint=self.joints[0]
            joint.set_angle(angle)
        elif action == 'UP1' or action == 'DOWN1' #first part of manipulator goes up/down
            joint=self.joints[1]
            joint.set_angle(angle)
        elif action == 'UP2' or action == 'DOWN2' #second part of manipulator goes up/down
            joint=self.joints[2]
            joint.set_angle(angle)
        elif action == 'RIGHT2' or action == 'LEFT2' #rotates gripper
            joint=self.joints[3]
            joint.set_angle(angle)
        elif action == 'OPEN' or 'GRAB' #not sure
            joint=self.jonts[4]
            joint.set_angle(angle)
            joint=self.jonts[5]
            joint.set_angle(angle)

    def reset_motor(self, number):
        joint=self.joints[number]
        if isinstance(joint, StepperMotor):
            joint.reset()

    def reset_all_motors(self):
        for i in range(len(self.joints)):
            if isinstance(self.joints[i], StepperMotor):
                self.joints[i].reset()
