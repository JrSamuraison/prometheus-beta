import pytest
from src.vowel_consonant_counter import count_vowels_consonants

def test_basic_counting():
    """Test basic vowel and consonant counting."""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_mixed_case():
    """Test counting with mixed case letters."""
    result = count_vowels_consonants("HeLLo")
    assert result == {'vowels': 2, 'consonants': 3}

def test_empty_string():
    """Test empty string returns zero counts."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_special_characters():
    """Test string with special characters and spaces."""
    result = count_vowels_consonants("hello, world! 123")
    assert result == {'vowels': 3, 'consonants': 3}

def test_only_vowels():
    """Test a string with only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test a string with only consonants."""
    result = count_vowels_consonants("rhythm")
    assert result == {'vowels': 0, 'consonants': 6}

def test_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)
        count_vowels_consonants(None)
        count_vowels_consonants(["hello"])