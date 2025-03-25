import pytest
from src.palindromic_substrings import find_palindromic_substrings

def test_find_palindromic_substrings_basic():
    """Test basic palindrome detection"""
    assert set(find_palindromic_substrings("aaa")) == set(['a', 'aa', 'aaa'])
    assert set(find_palindromic_substrings("abc")) == set(['a', 'b', 'c'])

def test_find_palindromic_substrings_longer():
    """Test longer strings with multiple palindromes"""
    result = set(find_palindromic_substrings("abcba"))
    expected = set(['a', 'b', 'c', 'bcb', 'abcba'])
    assert result == expected

def test_find_palindromic_substrings_empty():
    """Test empty string input"""
    assert find_palindromic_substrings("") == []

def test_find_palindromic_substrings_single_char():
    """Test single character input"""
    assert set(find_palindromic_substrings("x")) == set(['x'])

def test_find_palindromic_substrings_two_chars():
    """Test two character inputs"""
    assert set(find_palindromic_substrings("ab")) == set(['a', 'b'])
    assert set(find_palindromic_substrings("aa")) == set(['a', 'aa'])

def test_find_palindromic_substrings_sorted():
    """Test that results are sorted by length"""
    result = find_palindromic_substrings("racecar")
    assert result == ['r', 'a', 'c', 'e', 'r', 'ac', 'ce', 'ca', 'aca', 'racecar']

def test_find_palindromic_substrings_special_chars():
    """Test with special characters"""
    result = set(find_palindromic_substrings("a!b@c#"))
    expected = set(['a', 'b', 'c', '!', '@', '#'])
    assert result == expected