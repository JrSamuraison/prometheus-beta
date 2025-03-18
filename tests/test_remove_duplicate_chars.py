import pytest
from src.remove_duplicate_chars import remove_duplicates_over_threshold

def test_remove_duplicates_over_threshold():
    # Test cases with varying scenarios
    assert remove_duplicates_over_threshold("aabbcccd") == "aabbcd"
    assert remove_duplicates_over_threshold("aaabbbccc") == ""
    assert remove_duplicates_over_threshold("abcde") == "abcde"
    
    # Edge cases
    assert remove_duplicates_over_threshold("") == ""
    assert remove_duplicates_over_threshold("aaa") == "aa"
    
    # Mixed case and special characters
    assert remove_duplicates_over_threshold("AaaBbbCcc") == "AaaBbb"
    assert remove_duplicates_over_threshold("a!a!a!b") == "a!a!b"
    
    # Consecutive and non-consecutive duplicates
    assert remove_duplicates_over_threshold("aabccddee") == "aabccddee"

def test_remove_duplicates_order_preservation():
    # Ensure original order is maintained
    assert remove_duplicates_over_threshold("abcaaabbcccd") == "abcaabbcd"

def test_no_modification_for_minimal_duplicates():
    # Characters that appear 1-2 times should remain
    assert remove_duplicates_over_threshold("aabbccdd") == "aabbccdd"