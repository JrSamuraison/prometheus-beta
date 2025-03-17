import pytest
from src.celsius_to_fahrenheit import celsius_to_fahrenheit

def test_positive_celsius():
    """Test conversion of positive temperatures."""
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(37) == 98.6

def test_negative_celsius():
    """Test conversion of negative temperatures."""
    assert celsius_to_fahrenheit(-40) == -40.0
    assert pytest.approx(celsius_to_fahrenheit(-273.15), abs=0.01) == -459.67

def test_float_celsius():
    """Test conversion of float temperatures."""
    assert round(celsius_to_fahrenheit(25.5), 1) == 77.9

def test_type_error():
    """Test that TypeError is raised for invalid input types."""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([1, 2, 3])