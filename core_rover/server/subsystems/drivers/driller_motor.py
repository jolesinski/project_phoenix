from subsystems.fieldbus import InvalidControllerParametersError
from subsystems.drivers.base import BaseDriver


class DrillerMotor(BaseDriver):
    def __init__(self, address, driller_num):
        BaseDriver.__init__(self, address)
        self.driller_num = driller_num

    def echo(self):
        response_dict = self._request(command='\xff')
        return response_dict

    def start(self):
        response_dict = self._request(command='\x01', params=[self.driller_num])
        return response_dict

    def stop(self):
        response_dict = self._request(command='\x02', params=[self.driller_num])
        return response_dict

    def set_power(self, power):
        response_dict = self._request(command='\x04', params=[power, self.driller_num])
        return response_dict

    def set_direction(self, direction):
        if direction in [-1, 1]:
            response_dict = self._request(command='\x08', params=[direction, self.driller_num])
            return response_dict
        else:
            error_message = 'Invalid direction value for BLDC motor controller'
            raise InvalidControllerParametersError(message=error_message)