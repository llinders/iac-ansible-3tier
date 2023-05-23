import json
import pytest
from unittest import mock
from utils.data.ip_data_utils import remove_ips

# Mock the file operations
@mock.patch('builtins.open', create=True)
def test_remove_ips(mock_open):
    # Mock the file contents
    mock_file = mock_open.return_value
    mock_file.read.return_value = '["10.0.0.1", "10.0.0.2", "10.0.0.3"]'

    # Define the input and expected output
    ip_list = ["10.0.0.2", "10.0.0.3"]
    expected_ip_data = ["10.0.0.1"]

    # Call the function
    remove_ips(ip_list)

    # Check if the file was opened and written correctly
    mock_open.assert_called_once_with('__AVAILABLE_IP_ADDRESSES_FILE__', 'w')
    mock_file.write.assert_called_once_with(json.dumps(expected_ip_data))

# Run the test
pytest.main()
