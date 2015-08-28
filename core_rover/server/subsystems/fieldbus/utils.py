from array import array

def generate_crc8(message):
    feedback_bit = 0
    crc8_result = 0
    for byte in message:
        for _ in range(8):
            feedback_bit = (crc8_result & 0x01)
            crc8_result >>= 1
            if (feedback_bit ^ (byte & 0x01)):
                crc8_result ^= 0x8c
            byte >>= 1;
    return crc8_result


class ReadTimeout(Exception):
    def __init__(self, message=None):
        self.message = message or 'Timeout error'


class CommunicationError(Exception):
    def __init__(self, message=None):
        self.message = message or 'Communication error'


class InvalidControllerParametersError(Exception):
    def __init__(self, message=None):
        self.message = message or 'Invalid controller parameters'
