import pytest
from src.palindrome import is_palindrome

def test_is_palindrome_basic():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_is_palindrome_case_insensitive():
    """Test that function is case-insensitive"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_is_palindrome_with_punctuation():
    """Test palindromes with punctuation and spaces"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_is_palindrome_edge_cases():
    """Test edge cases"""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Just a space
    assert is_palindrome("!@#$%^&*()") == True  # Only special characters
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("ab") == False  # Two different characters

def test_is_palindrome_with_numbers():
    """Test palindromes with numbers"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False