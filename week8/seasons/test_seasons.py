from seasons import calculate_age_in_minutes
import pytest

def test_calculate_age_in_minutes():
    assert calculate_age_in_minutes("2000-01-01") > 0

def test_invalid_date():
    with pytest.raises(SystemExit):
        calculate_age_in_minutes("invalid date")