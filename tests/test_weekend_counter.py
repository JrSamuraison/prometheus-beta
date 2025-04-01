import pytest
from src.weekend_counter import count_weekends_in_month

def test_typical_month():
    """Test a typical month with both weekend and weekdays."""
    # January 2023 has 9 weekend days
    assert count_weekends_in_month(2023, 1) == 9

def test_february_leap_year():
    """Test February in a leap year."""
    # February 2024 (leap year) has 8 weekend days
    assert count_weekends_in_month(2024, 2) == 8

def test_february_non_leap_year():
    """Test February in a non-leap year."""
    # February 2023 (non-leap year) has 8 weekend days
    assert count_weekends_in_month(2023, 2) == 8

def test_month_with_31_days():
    """Test a month with 31 days."""
    # March 2023 has 8 weekend days
    assert count_weekends_in_month(2023, 3) == 8

def test_month_with_30_days():
    """Test a month with 30 days."""
    # April 2023 has 10 weekend days
    assert count_weekends_in_month(2023, 4) == 10

def test_invalid_month_low():
    """Test handling of invalid low month input."""
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 0)

def test_invalid_month_high():
    """Test handling of invalid high month input."""
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        count_weekends_in_month(2023, 13)