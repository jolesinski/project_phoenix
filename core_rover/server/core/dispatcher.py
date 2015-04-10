# =============================================================================
# File name: dispatcher.py
# Authors: Bartlomiej Lisiecki
# Python version: 2.7
# =============================================================================

"""
    JSON-RPC dispatcher module.

    Dispatcher with defined API for communication between client and server.
"""

from jsonrpc import JSONRPCResponseManager, dispatcher
from utils import throwInvalidParams, isStrictInt
from werkzeug.wrappers import Request, Response


#  Methods defined for server.
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

    # Check if params are correct
    if not (isStrictInt(joint) and isinstance(angle, float)):
        # If not, send Invalid params error to client
        throwInvalidParams()

    # Body
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

    # Check if params are correct
    if not isStrictInt(joint):
        # If not, send Invalid params error to client
        throwInvalidParams()

    # Set initial angle to default value
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

    # Check if params are correct
    if not (isStrictInt(joint) and isStrictInt(speed)):
        # If not, send Invalid params error to client
        throwInvalidParams()

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

    # Check if params are correct
    if not isStrictInt(joint):
        # If not, send Invalid params error to client
        throwInvalidParams()

    # Set initial angle to default value
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

    # Check if params are correct
    if not (isinstance(x, float) and
            isinstance(y, float) and
            isinstance(z, float)):
        # If not, send Invalid params error to client
        throwInvalidParams()

    # Body
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

    # Set initial angle to default value
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

    # Check if params are correct
    if not isinstance(open, bool):
        # If not, send Invalid params error to client
        throwInvalidParams()

    # Body
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

    # Check if params are correct
    if not (isStrictInt(wheel) and isStrictInt(speed)):
        # If not, send Invalid params error to client
        throwInvalidParams()

    # Body
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

    # Check if params are correct
    if not isStrictInt(wheel):
        # If not, send Invalid params error to client
        throwInvalidParams()

    # Set initial angle to default value
    speed = 0
    return speed


# Dispatcher application
@Request.application
def application(request):
    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')
