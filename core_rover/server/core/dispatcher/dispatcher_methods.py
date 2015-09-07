from core_rover.server.core.dispatcher.dispatcher import MethodDispatcher
from core_rover.server.core.utils import InvalidParametersException, is_strict_int
# subsystems - dirty
from core_rover.server.subsystems.manipulator import Manipulator
from core_rover.server.subsystems.camera import Gimbal
from core_rover.server.subsystems.location.regulator import Regulator
from core_rover.server.subsystems.chassis.chassis import Chassis
from core_rover.server.subsystems.camera.usb_cam import USBStreamer

dispatcher = MethodDispatcher()

# subsystems - dirty
manipulator = Manipulator()
gimbal = Gimbal()
regulator = Regulator()
chassis_driver = Chassis
USBCam = USBStreamer(rtp='192.168.2.13', port=8074)

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

    # add validation
    response = manipulator.joints[joint].set_angle(angle)
    status_code = response.status
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

    # TODO: add validation
    manipulator.set_effector_position(x, y, z)
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
    # TODO: add validatioon
    manipulator.gripper.open()
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

@dispatcher.add_method
def setCameraOrientation(angle_x, angle_z):
    r"""Sets orientation of IP camera gimbal.

    Parameters
    ----------
    angle_x : float
        Target angle around x axis in radians.
    angle_z : float
        Target angle around z axis in radians.

    Returns
    -------
    status_code : int
        Returns 0, because we want to handle errors and thats impossible with
        notifications.
    """

    if not (isinstance(angle_x, float) and isinstance(angle_z, float)):
        raise InvalidParametersException()

    #add validation
    response = gimbal.set_orientation(angle_x, angle_z)
    status_code = response.status
    return status_code

@dispatcher.add_method
def getGPS():
    r"""Returns latitude and longitude of the rover.
 
     Returns
     -------
     coordinates : list
         Latitude and longitude of the rover in a form of [a, b] list, where a,
         b are float values.
     """
    coordinates = regulator.gps.getGPS()
    return coordinates


@dispatcher.add_method
def chassisDrive(speed, direction):
    r"""Drives the rover based on speed and direction params
    The speed and direction params are -1.0 to 1.0 values, where 0.0 means all drives stopped
    and not turning.

    Parameters
    ----------
    speed : floating point number
        Speed of rover 1.0 is max forward, -1.0 is max backwards
    direction : floating point number
        Direction of curve, -1.0 is max to the left, 1.0 max to the right

    Returns
    -------
    status_code = 0
    """
    chassis_driver.drive(speed, direction)
    status_code = 0
    return status_code


@dispatcher.add_method
def chassisStop():
    r"""Stops all motors

    Returns
    -------
    status_code = 0
    """

    chassis_driver.stop()
    status_code = 0
    return status_code


@dispatcher.add_method
def USBCamStartStream(camera):
    r"""
    Starts camera streaming -> need to know params for vlc from camera.sdp file

    Parameters
    ----------
    camera : int
        Number of camera from /dev/video*
    """

    if not is_strict_int(camera):
        raise InvalidParametersException()

    USBCam.startStream(camera)


@dispatcher.add_method
def USBCamStopStream():
    r""" Stops all streaming from USB

    Returns
    -------
    status_code : int
    """
    USBCam.stopStream()
    status_code = 0
    return status_code


@dispatcher.add_method
def USBCamSwitchCamera(camera):
    r"""Switch currently streaming cam

    Parameters
    ---------
    camera : int
        Number of camera from /dev/video*
    """
    if not is_strict_int(camera):
        raise InvalidParametersException()

    USBCam.switchCamera(camera)


@dispatcher.add_method
def USBCamSetInputResolution(resolution):
    r"""Change resolution of streaming

    Params:
    ------
    resolution : string
        New stream resolution in format: "320x240"
    """

    USBCam.setInputResolution(resolution)


@dispatcher.add_method
def USBCamSetOutputResolution(resolution):
    r"""Change resolution of displaying

    Params:
    ------
    resolution : string
        New stream resolution in format: "320x240"
    """
    USBCam.setOutputResolution(resolution)


@dispatcher.add_method
def USBCamGetStreamResolution():
    r"""Streaming resolution getter

    Returns
    ------
    resolution : string
        Resolution in format: "320x240"
    """

    resolution = USBCam.getStreamResolution()
    return resolution
>>>>>>> master
