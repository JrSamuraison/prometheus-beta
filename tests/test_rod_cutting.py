import pytest
from src.rod_cutting import rod_cutting

def test_basic_rod_cutting():
    """Test basic rod cutting scenario"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10  # Cutting rod of length 4

def test_single_length_rod():
    """Test rod cutting for a single length"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 1) == 1

def test_full_rod_length():
    """Test rod cutting for the full length of the price list"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 8) == 22  # Updated to match optimal solution

def test_zero_length_rod():
    """Test rod cutting for zero length"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 0) == 0

def test_invalid_rod_length():
    """Test rod cutting when rod length exceeds price list"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    with pytest.raises(ValueError):
        rod_cutting(prices, 9)

def test_empty_prices():
    """Test rod cutting with empty price list"""
    assert rod_cutting([], 5) == 0

def test_complex_rod_cutting():
    """Test a more complex rod cutting scenario"""
    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 12  # Updated to match optimal solution