from core_rover.server.subsystems.drivers.base import BaseDriver


class StepperMotor(BaseDriver):
    def move(self, steps=0):
        response_dict = self._request(command=1, params=[steps])
        return response_dict

    def stop(self):
        response_dict = self._request(command=2)
        return response_dict

    def pause(self):
        response_dict = self._request(command=3)
        return response_dict

    def unpause(self):
        response_dict = self._request(command=4)
        return response_dict

    def set_mode(self, mode=1):
        response_dict = self._request(command=5, params=[mode])
        return response_dict

    def set_speed(self, steps_per_sec=0):
        response_dict = self._request(command=6, params=[steps_per_sec])
        return response_dict

    def limit_current(self, mode=0):
        response_dict = self._request(command=7, params=[mode], respond=False)
        return response_dict

    def set_limit_temperature(self, degrees=0):
        response_dict = self._request(command=8, params=[degrees])
        return response_dict

    def get_motor_temperature(self):
        response_dict = self._request(command=9)
        return response_dict

    def reset(self):
        password = 'ASDF'
        response_dict = self._request(command=66, params=[password], respond=False)
        return response_dict

    def report_errors(self):
        response_dict = self._request(command=80)
        return response_dict

    def present(self):
        response_dict = self._request(command=255)
        return response_dict