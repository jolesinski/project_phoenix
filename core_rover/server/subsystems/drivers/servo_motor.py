from core_rover.server.subsystems.drivers.base import BaseDriver


class ServoMotor(BaseDriver):
    def servo_set_position(self, position=0):
        response_dict = self._request(command=20, params=[position])
        return response_dict

    def set_angle(self, angle=0):
        position = self.servo_angle_to_position(angle)
        return self.servo_set_position(position)

    def servo_angle_to_position(self, angle):
        #DO SOME MAGIC HERE
        raise NotImplementedError

    def present(self):
        response_dict = self._request(command=255)
        return response_dict