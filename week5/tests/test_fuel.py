from fuel import convert, gauge
import pytest

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("-2/7")
    with pytest.raises(ValueError):
        convert("8/-9")
    with pytest.raises(ValueError):
        convert("1.4/6")
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert():
    assert convert("3/4") == 75
    assert convert("2/3") == 67
    assert convert("1/4") == 25

def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge():
    assert gauge(56) == "56%"
    assert gauge(31) == "31%"
    assert gauge(77) == "77%"