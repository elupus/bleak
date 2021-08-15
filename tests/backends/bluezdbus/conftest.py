
import pytest
from unittest.mock import patch, Mock

from dbus_next.message import Message
from dbus_next.aio import MessageBus
from bleak.backends.bluezdbus.client import BleakClientBlueZDBus


@pytest.fixture(autouse=True)
def fixture_popen():
    with patch('subprocess.Popen') as mock_subproc_popen:
        process_mock = Mock()
        attrs = {'communicate.return_value': (b'bluetoothctl: 5.55', b'')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        yield process_mock
