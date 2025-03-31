import time
from datetime import datetime
import pytest
from timestamp_converter.converter import unix_to_timestamp, is_unixtimestamp

def test_unix_to_timestamp():
    # Test with a known Unix timestamp
    unixtime = 1609459200  # Corresponds to 2021-01-01T00:00:00
    expected = datetime.fromtimestamp(unixtime).isoformat()
    assert unix_to_timestamp(unixtime) == expected

def test_unix_to_timestamp_current_time():
    # Test conversion of current time; the result should match the beginning of the ISO string.
    now = time.time()
    expected_prefix = datetime.fromtimestamp(now).isoformat()[:16]
    assert unix_to_timestamp(now).startswith(expected_prefix)

def test_unix_to_timestamp_invalid_input():
    # Test that a TypeError is raised when input is not a number.
    with pytest.raises(TypeError):
        unix_to_timestamp("not a number")

def test_is_unixtimestamp_valid():
    # Valid Unix timestamp
    assert is_unixtimestamp(1609459200) is True

def test_is_unixtimestamp_invalid_type():
    # Non-integer should return False
    assert is_unixtimestamp("1234567890") is False

def test_is_unixtimestamp_out_of_range():
    # Extremely large number likely raises an exception
    assert is_unixtimestamp(999999999999999) is False
