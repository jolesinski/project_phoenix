from jsonrpc import JSONRPCResponseManager, dispatcher
from utils import InvalidParametersException, is_strict_int
from werkzeug.wrappers import Request, Response


@dispatcher.add_method
def setJointAngle(joint, angle):
    r"""Sets angle of a specified joint.

    Parameters
    ----------
    joint : int
        Joint selector.
    angle : float
        Target angle in radians.

    Returns
    -------
    status_code : int
        Returns 0, because we want to handle errors and thats impossible with
        notifications.
    """

    if not (is_strict_int(joint) and isinstance(angle, float)):
        raise InvalidParametersException()
    status_code = 0
    return status_code


@dispatcher.add_method
def getJointAngle(joint):
    r"""Returns angle of a specified joint.

    Parameters
    ----------
    joint : int
        Joint selector.

    Returns
    -------
    angle : float
        Angle of a specified joint in radians.
    """

    if not is_strict_int(joint):
        raise InvalidParametersException()

    angle = 0.0
    return angle


@dispatcher.add_method
def setJointSpeed(joint, speed):
    r"""Sets speed of a specified joint.

    Parameters
    ----------
    joint : int
        Joint selector.
    speed : int
        Target speed in scale 1-100.

    Returns
    -------
    status_code : int
        Returns 0, because we want to handle errors and thats impossible with
        notifications.
    """

    if not (is_strict_int(joint) and is_strict_int(speed)):
        raise InvalidParametersException()

    # Body
    status_code = 0
    return status_code


@dispatcher.add_method
def getJointSpeed(joint):
    r"""Returns speed of a specified joint.

    Parameters
    ----------
    joint : int
        Joint selector.

    Returns
    -------
    speed: int
        Speed of a specified joint in scale 1-100.
    """

    if not is_strict_int(joint):
        raise InvalidParametersException()

    speed = 0
    return speed


@dispatcher.add_method
def setCartesianPosition(x, y, z):
    r"""Sets cartesian position of gripper.

    Parameters
    ----------
    x, y, z : float
        Target cartesian coordinates (horizontal, vertical, depth).

    Returns
    -------
    status_code : int
        Returns 0, because we want to handle errors and thats impossible with
        notifications.
    """

    if not (isinstance(x, float) and
            isinstance(y, float) and
            isinstance(z, float)):
        raise InvalidParametersException()

    status_code = 0
    return status_code


@dispatcher.add_method
def getCartesianPosition():
    r"""Returns cartesian position of a gripper.

    Returns
    -------
    cartesianPos : list
        Cartesian position of a gripper in a form of [x, y, z] list, where x,
        y and z are float values.
    """

    cartesianPos = [0.0, 0.0, 0.0]
    return cartesianPos


@dispatcher.add_method
def setGripper(open):
    r"""Opens/closes gripper.

    Parameters
    ----------
    open : bool
        Specifies if gripper should bo opened (True) or closed (False)

    Returns
    -------
    status_code : int
        Returns 0, because we want to handle errors and thats impossible with
        notifications.
    """

    if not isinstance(open, bool):
        raise InvalidParametersException()

    status_code = 0
    return status_code


@dispatcher.add_method
def setWheelSpeed(wheel, speed):
    r"""Sets speed of a specified wheel of rover.

    Parameters
    ----------
    wheel : int
        Wheel selector.
    speed : int
        Target speed in scale 1-100.

    Returns
    -------
    status_code : int
        Returns 0, because we want to handle errors and thats impossible with
        notifications.
    """

    if not (is_strict_int(wheel) and is_strict_int(speed)):
        raise InvalidParametersException()

    status_code = 0
    return status_code


@dispatcher.add_method
def getWheelSpeed(wheel):
    r"""Returns speed of a specified wheel.

    Parameters
    ----------
    wheel : int
        Wheel selector.

    Returns
    -------
    speed: int
        Speed of a specified wheel in radians.
    """

    if not is_strict_int(wheel):
        raise InvalidParametersException()

    speed = 0
    return speed


@Request.application
def application(request):
    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')
