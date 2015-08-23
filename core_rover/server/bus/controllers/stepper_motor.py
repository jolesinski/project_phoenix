from .base import BaseController


class StepperMotor(BaseController):

    def move(self, steps=0):
        # prepare data for move command
        self._send_frame(data=data)
        # we probably need to analyze return msg
        # and set status code
        status_code = 0
        return status_code

    def stop(self, steps=0):
        # prepare data for stop command
        self._send_frame(data=data)

    def pause(self, steps=0):
        # prepare data for pause command
        self._send_frame(data=data)

    def unpause(self, steps=0):
        # prepare data for unpause command
        self._send_frame(data=data)

    def set_mode(self, steps=0):
        # prepare data for move command
        self._send_frame(data=data)

    def set_speet(self, steps=0):
        # prepare data for stop command
        self._send_frame(data=data)

    def limit_current(self, steps=0):
        # prepare data for pause command
        self._send_frame(data=data)

    def set_limit_temperature(self, steps=0):
        # prepare data for unpause command
        self._send_frame(data=data)

    def get_motor_temperature(self, steps=0):
        # prepare data for move command
        self._send_frame(data=data)

    def servo_set_position(self, steps=0):
        # prepare data for stop command
        self._send_frame(data=data)

    def reset(self, steps=0):
        # prepare data for pause command
        self._send_frame(data=data)

    def report_errors(self, steps=0):
        # prepare data for unpause command
        self._send_frame(data=data)

    def present(self, steps=0):
        # prepare data for unpause command
        self._send_frame(data=data)

