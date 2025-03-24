import pytest
from src.palindrome_number import is_palindrome_number

def test_positive_palindrome_numbers():
    """Test various positive palindrome numbers."""
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(1) == True
    assert is_palindrome_number(22) == True
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(45654) == True

def test_non_palindrome_numbers():
    """Test various non-palindrome numbers."""
    assert is_palindrome_number(10) == False
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(456) == False
    assert is_palindrome_number(1234) == False

def test_negative_numbers():
    """Test that negative numbers are not palindromes."""
    assert is_palindrome_number(-121) == False
    assert is_palindrome_number(-11) == False
    assert is_palindrome_number(-1) == False

def test_zero():
    """Test zero as a special case."""
    assert is_palindrome_number(0) == True

def test_invalid_input():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        is_palindrome_number("121")
    
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    
    with pytest.raises(TypeError):
        is_palindrome_number(None)