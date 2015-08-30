from jsonrpc.exceptions import JSONRPCDispatchException


class InvalidParametersException(JSONRPCDispatchException):

    def __init__(self):
        self.code = -32602
        self.message = "Invalid params"


def is_strict_int(value):
    r"""Checks if values type is int (in python isinstance(True/False, int) returns True).

    Params
    ------
        value: any-type
            Value to be tested.

    Returns
    -------
        bool
            True if value is int and is not bool.
    """