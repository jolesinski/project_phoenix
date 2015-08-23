from server.bus import (
        InvalidControllerParametersError,
        Request,
)
from server.bus.controllers import BaseController


class BLDCMotor(BaseController):

    def echo(self, address):
        request = Request(
                address=address,    # we need some address standatization
                respond=True,   # I think we always want the response from controller?
                command=0, # needs to be changed
                params=[],
        )
        # calculate crc8, interface really sucks, we need to change this guys ASAP
        response_dict = self._send_frame(data=request.str)
        # we need to discuss what the response for base will look like
        # because we have status of bus and response from controller
        # This probably wont work but I cant tell without full setup
        # (server, client and controller)
        return response_dict

    def start(self, address):
        request = Request(
                address=address,
                respond=True,   # I think we always want the response from controller?
                command='\x01', # needs to be changed
                params=[],
        )
        # calculate crc8, interface really sucks, we need to change this guys ASAP
        response_dict = self._send_frame(data=request.str)
        # we need to discuss what the response for base will look like
        # because we have status of bus and response from controller
        # This probably wont work but I cant tell without full setup
        # (server, client and controller)
        return response_dict

    def stop(self, address):
        request = Request(
                address=address,
                respond=True,   # I think we always want the response from controller?
                command='\x02', # needs to be changed
                params=[],
        )
        # calculate crc8, interface really sucks, we need to change this guys ASAP
        response_dict = self._send_frame(data=request.str)
        # we need to discuss what the response for base will look like
        # because we have status of bus and response from controller
        # This probably wont work but I cant tell without full setup
        # (server, client and controller)
        return response_dict

    def set_power(self, address, power):
        # we need to have validation for power, but first we need to estabilish
        # some protocol so that i know how to validate it
        request = Request(
                address=address,
                respond=True,   # I think we always want the response from controller?
                command='\x04', # needs to be changed
                params=[power],
        )
        # calculate crc8, interface really sucks, we need to change this guys ASAP
        response_dict = self._send_frame(data=request.str)
        # we need to discuss what the response for base will look like
        # because we have status of bus and response from controller
        # This probably wont work but I cant tell without full setup
        # (server, client and controller)
        return response_dict

    def set_direction(self, address, direction):
        # probably needs better validation
        if direction in [-1, 1]:
            request = Request(
                    address=address,
                    respond=True,   # I think we always want the response from controller?
                    command='\x08', # needs to be changed
                    params=[direction],
            )
            # calculate crc8, interface really sucks, we need to change this guys ASAP
            response_dict = self._send_frame(data=request.str)
            # we need to discuss what the response for base will look like
            # because we have status of bus and response from controller
            # This probably wont work but I cant tell without full setup
            # (server, client and controller)
            return response_dict
        else:
            error_message = 'Invalid direction value for BLDC motor controller'
            raise InvalidControllerParametersError(message=error_message)

