from array import array

from rs485.utils import generate_crc8

# definitely needs refactoring (legacy code)
class Response:
    def __init__(self, address=-1, command=-1, data=None, crc8=-1):
        self.address = address
        self.command = command
        self.crc8 = crc8

        if data is None:
            self.data = []
        else:
            self.data = data

    def calculate_crc8(self):
        temp = array('B')
        temp.fromlist([self.address, self.command, len(self.data)] + self.data)
        return generate_crc8(temp);

    def str(self):
        s = "%c%c%c" % (self.address, self.command, len(self.data))
        for i in range(len(self.data)):
            s += "%c" % (self.data[i])
        s += "%c" % (self.crc8)
        return s

