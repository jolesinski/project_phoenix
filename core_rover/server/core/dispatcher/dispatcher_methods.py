from jsonrpc import JSONRPCResponseManager
from werkzeug.wrappers import Request, Response

from server.core.utils import InvalidParametersException, is_strict_int
from server.core.dispatcher.dispatcher import MethodDispatcher
from server.bus.utils import InvalidControllerParametersError

dispatcher = MethodDispatcher()

# we could also move this methods to a standalone class
# and add them as static (they cant accept self parameter)
# but that would still require adding them to one dispatcher
@dispatcher.add_method
def stepper_motor_move(steps):
    return dispatcher.stepper_motor.move()

@dispatcher.add_method
def bldc_echo(address):
    return dispatcher.bldc_motor.echo(address=address)

@dispatcher.add_method
def bldc_start(address):
    return dispatcher.bldc_motor.start(address=address)

@dispatcher.add_method
def bldc_stop(address):
    return dispatcher.bldc_motor.stop(address=address)

@dispatcher.add_method
def bldc_set_power(address, power):
    try:
        dispatcher.bldc_motor.set_power(address=address, power=power)
    except InvalidControllerParametersError as error:
        raise InvalidParametersException(message=error.message)

@dispatcher.add_method
def bldc_set_direction(address, direction):
    try:
        dispatcher.bldc_motor.set_direction(address=address, power=power)
    except InvalidControllerParametersError as error:
        raise InvalidParametersException(message=error.message)

