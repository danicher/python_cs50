from working import convert
import pytest

def test_valid_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 1:45 PM") == "10:30 to 13:45"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1 PM to 11 PM") == "13:00 to 23:00"
    assert convert("12:15 AM to 12:45 PM") == "00:15 to 12:45"

def test_invalid_time_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("9 AM to 17 PM")

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
