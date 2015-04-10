from jsonrpc.exceptions import JSONRPCDispatchException


# Functions throwing errors used in dispatch functions
def throwInvalidParams():
    r"""Sets error in response to Invalid params error.

    Raises
    ------
        JSON-RPC Dispatch Exception with code and message for Invalid params
    """
    raise JSONRPCDispatchException(code=-32602,
                                   message="Invalid params")


def isStrictInt(value):
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
    return isinstance(value, int) and not isinstance(value, bool)
