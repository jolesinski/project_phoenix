from array import array

from core_rover.server.subsystems.fieldbus.utils import generate_crc8


# definitely needs refactoring (legacy code)
class RequestFrame:
    def __init__(self, address, respond, command, params=[]):
        #using direct access to __dict__ prevents from premature crc8 calculation using __setattr__ during initialization
        self.__dict__['address'] = address
        if respond:
            self.__dict__['respond'] = 1
        else:
            self.__dict__['respond'] = 0
        self.__dict__['command'] = command
        self.__dict__['params'] = params
        self.__dict__['crc8'] = self.calculate_crc8()

    def __setattr__(self, name, value):
        """
        Handles auto-update of Crc8 when some values change
        """
        self.__dict__[name] = value
        self.__dict__['crc8'] = self.calculate_crc8()

    def calculate_crc8(self):
        temp = array('B')
        temp.fromlist([(self.address << 1) + self.respond, self.command,
                       len(self.params)] + self.params)
        return generate_crc8(temp)

    def str(self):
        """"
        Returns ASCII string corresponding to HEX values of encoded message.
        Not the same as __str__()
        """
        addr = (self.address << 1) + self.respond
        s = "%c%c%c" % (addr, self.command, len(self.params))

        for i in range(len(self.params)):
            s += "%c" % (self.params[i])

        s += "%c" % (self.crc8)
        return s

    @classmethod
    def str_2_request(cls, string):
        binary = [ord(char) for char in string]
        address = binary[0]
        respond = address & 0x01
        address >>= 1
        command = binary[1]
        params = []
        for i in range(binary[2]):
            params.append(binary[3+i])
        return cls(address, respond, command, params)


# definitely needs refactoring (legacy code)
class ResponseFrame:
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
        return generate_crc8(temp)

    def str(self):
        s = "%c%c%c" % (self.address, self.command, len(self.data))
        for i in range(len(self.data)):
            s += "%c" % (self.data[i])
        s += "%c" % self.crc8
        return s