import sys
import time

import enum

import serial
from core_rover.server.subsystems.fieldbus.frame import RequestFrame, ResponseFrame
from .utils import CommunicationError


class FieldbusStatuses(enum.Enum):
    OK = '\x00'
    RD_TIMEOUT = '\x01'
    WR_TIMEOUT = '\x02'
    CRC_ERR = '\x03'
    PORT_ERR = '\xFF'


class Fieldbus():
    def __init__(self, port, baud=9600, read_timeout=10.0):
        self._initialize_serial_port(
            port=port, baud=baud, timeout=read_timeout,
        )
        self._read_timeout = read_timeout
        self.status = FieldbusStatuses.OK
        self._isOpen = False
        self.open_port()

    def open_port(self):
        try:
            if self._isOpen is False:
                self._port.open()
            else:
                print 'Port already open'
        except serial.SerialException:
            # not sure if its good idea to disconnect here, any ideas?
            # also add debug instead of print
            print 'Cannot connect to serial device'
            sys.exit(0)
        self._isOpen = True

    def close_port(self):
        self._isOpen = False
        self._port.close()

    def request(self, address, respond, command, params=[]):
        self.status = FieldbusStatuses.OK
        request = RequestFrame(address, respond, command, params)
        print repr(request.str())
        response = None
        try:
            self._send_data_to_bus(request.str)
        except serial.SerialTimeoutException:
            self.status = FieldbusStatuses.WR_TIMEOUT
            # add log.error
        except:
            # add log.error
            self.status = FieldbusStatuses.PORT_ERR
        finally:
            try:
                response = self._get_response()
            except serial.SerialReadTimeoutException:
                # add log.error
                self.status = FieldbusStatuses.RD_TIMEOUT
            except CommunicationError:
                # add log.error
                self.status = FieldbusStatuses.CRC_ERR
            except:
                # duplicated, refactor later
                # add log.error
                self.status = FieldbusStatuses.PORT_ERR
        if response is not None:
            data = response.data
        else:
            data = None
        return dict(data=data, status=self.status)

    def _initialize_serial_port(self, port, baud, timeout):
        self._port = serial.Serial()
        self._port.port = port
        self._port.baudrate = baud
        self._port.parity = serial.PARITY_NONE
        self._port.bytesize = serial.EIGHTBITS
        self._port.stopbits = serial.STOPBITS_ONE
        self._port.timeout = timeout
        self._port.writeTimeout = 10.0

    def _set_parity_high(self):
        self._port.parity = serial.PARITY_MARK

    def _set_parity_low(self):
        self._port.parity = serial.PARITY_SPACE

    def _clear_buffers(self):
        self._port.flushInput()
        self._port.flushOutput()

    def _write_to_port(self, data):
        self._port.write(data)
        self._port.flush()

    def _send_data_to_bus(self, data):
        self._clear_buffers()
        self._set_parity_high()
        self._write_to_port(data[0])
        time.sleep(0.002)
        self._set_parity_low()
        self._write_to_port(data[1:])

    def _get_response(self):
        response = ResponseFrame()
        self._port.timeout = self._read_timeout
        response.address = ord(self._port.read(1))

        self._port.timeout = 0.5
        response.command = ord(self._port.read(1))
        data_count = ord(self._port.read(1))
        for _ in range(data_count):
            response.data.append(ord(self._port.read(1)))
        crc8 = ord(self._port.read(1))

        if crc8 == response.calculate_crc8():
            return response
        else:
            raise CommunicationError()

    #TODO: response validation