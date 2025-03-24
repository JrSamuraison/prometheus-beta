import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic LCS scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test when no common subsequence exists"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_one_empty_string():
    """Test LCS with one empty string"""
    assert longest_common_subsequence("", "ABCD") == ""
    assert longest_common_subsequence("ABCD", "") == ""

def test_both_empty_strings():
    """Test LCS with both empty strings"""
    assert longest_common_subsequence("", "") == ""

def test_partial_subsequence():
    """Test partial subsequence scenarios"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"
    assert longest_common_subsequence("XMJYAUZ", "MZJAWXU") == "MJAU"

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "ABC")

def test_case_sensitivity():
    """Test case sensitivity of LCS"""
    assert longest_common_subsequence("AbC", "aBC") == ""