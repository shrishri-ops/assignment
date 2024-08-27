# # test_cpu_monitor.py
# import pytest
# from unittest.mock import patch
# from server_monitoring import monitor_cpu

# @patch('psutil.cpu_percent')
# @patch('time.sleep', return_value=None)  # Mock sleep to avoid delays in tests
# def test_monitor_cpu(mock_sleep, mock_cpu_percent):
#     # Test case 1: CPU usage below the threshold
#     mock_cpu_percent.return_value = 50
#     with patch('builtins.print') as mock_print:
#         monitor_cpu(threshold=80, interval=0.1)  # Use a short interval for testing
#         mock_print.assert_not_called()  # No alert should be printed
    
#     # Test case 2: CPU usage above the threshold
#     mock_cpu_percent.return_value = 85
#     with patch('builtins.print') as mock_print:
#         monitor_cpu(threshold=80, interval=0.1)  # Use a short interval for testing
#         mock_print.assert_called_with('Alert! CPU usage exceeds threshold: 85%')

# @pytest.mark.parametrize("cpu_usage,expected_output", [
#     (30, False),  # No alert expected for usage below threshold
#     (85, True)    # Alert expected for usage above threshold
# ])
# @patch('psutil.cpu_percent')
# @patch('time.sleep', return_value=None)  # Mock sleep to avoid delays in tests
# def test_monitor_cpu_with_parameters(mock_sleep, mock_cpu_percent, cpu_usage, expected_output):
#     mock_cpu_percent.return_value = cpu_usage
#     with patch('builtins.print') as mock_print:
#         monitor_cpu(threshold=80, interval=0.1)
#         if expected_output:
#             mock_print.assert_called_with(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
#         else:
#             mock_print.assert_not_called()


import pytest
from unittest.mock import patch
from server_monitoring import monitor_cpu

@patch('psutil.cpu_percent')
@patch('time.sleep', return_value=None)
def test_monitor_cpu(mock_sleep, mock_cpu_percent):
    # Test case 1: CPU usage below the threshold
    mock_cpu_percent.return_value = 50
    result = monitor_cpu(threshold=80, interval=0.1)
    assert result is None  # No alert should be returned

@patch('psutil.cpu_percent')
@patch('time.sleep', return_value=None)
@pytest.mark.parametrize("cpu_usage,expected_output", [
    (30, None),  # No alert expected for usage below threshold
    (85, "Alert! CPU usage exceeds threshold: 85%")  # Alert expected for usage above threshold
])
def test_monitor_cpu_with_parameters(mock_sleep, mock_cpu_percent, cpu_usage, expected_output):
    mock_cpu_percent.return_value = cpu_usage
    result = monitor_cpu(threshold=80, interval=0.1)
    assert result == expected_output

@patch('psutil.cpu_percent', side_effect=KeyboardInterrupt)
def test_monitor_cpu_interrupt(mock_cpu_percent):
    result = monitor_cpu(threshold=80, interval=0.1)
    assert result == "Monitoring stopped by user."
