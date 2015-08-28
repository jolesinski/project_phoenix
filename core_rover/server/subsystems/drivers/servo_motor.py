from core_rover.server.subsystems.drivers.base import BaseDriver


class ServoMotor(BaseDriver):
    def servo_set_position(self, position=0):
        response_dict = self._request(command=20, params=[position])
        return response_dict

    def present(self):
        response_dict = self._request(command=255)
        return response_dict