import pytest
import mock

from server.bus.controllers import BLDCMotor
from server.bus import Request

class TestBLDCMotor(object):

    @pytest.fixture
    def controller(self):
        bus = mock.Mock()
        return BLDCMotor(bus=bus)

    @mock.patch.object(Request, 'str')
    @mock.patch.object(BLDCMotor, '_send_frame')
    def test_echo(self, send_frame_mock, request_str_mock, controller):
        result = controller.echo(address=11)
        send_frame_mock.assert_called_with(data=request_str_mock)
        assert result == send_frame_mock.return_value
