import pytest

from server.bus import FieldbusStatuses


class TestFieldbusStatuses(object):

    @pytest.fixture
    def fieldbus_statuses(self):
        return FieldbusStatuses

    def test_OK_status(self, fieldbus_statuses):
        assert hasattr(fieldbus_statuses, 'OK')
        assert fieldbus_statuses.OK == '\x00'

    def test_RD_TIMEOUT_status(self, fieldbus_statuses):
        assert hasattr(fieldbus_statuses, 'RD_TIMEOUT')
        assert fieldbus_statuses.RD_TIMEOUT == '\x01'

    def test_WR_TIMEOUT_status(self, fieldbus_statuses):
        assert hasattr(fieldbus_statuses, 'WR_TIMEOUT')
        assert fieldbus_statuses.WR_TIMEOUT == '\x02'

    def test_CRC_ERR_status(self, fieldbus_statuses):
        assert hasattr(fieldbus_statuses, 'CRC_ERR')
        assert fieldbus_statuses.CRC_ERR == '\x03'

    def test_PORT_ERR_status(self, fieldbus_statuses):
        assert hasattr(fieldbus_statuses, 'PORT_ERR')
        assert fieldbus_statuses.PORT_ERR == '\xFF'
