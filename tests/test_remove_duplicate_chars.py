import pytest
from src.remove_duplicate_chars import remove_duplicates_over_threshold

def test_remove_duplicates_over_threshold():
    # Test cases with varying scenarios
    assert remove_duplicates_over_threshold("aabbcccd") == "abcd"
    assert remove_duplicates_over_threshold("aaabbbccc") == ""
    assert remove_duplicates_over_threshold("abcde") == "abcde"
    
    # Edge cases
    assert remove_duplicates_over_threshold("") == ""
    assert remove_duplicates_over_threshold("aaa") == ""
    
    # Mixed case and special characters
    assert remove_duplicates_over_threshold("AaaBbbCcc") == ""
    assert remove_duplicates_over_threshold("a!a!a!b") == "b"
    
    # Consecutive and non-consecutive duplicates
    assert remove_duplicates_over_threshold("aabccddee") == "abcde"

def test_remove_duplicates_order_preservation():
    # Ensure original order is maintained
    assert remove_duplicates_over_threshold("abcaaabbcccd") == "abcd"

def test_no_modification_for_minimal_duplicates():
    # Characters that appear 1-2 times should remain
    assert remove_duplicates_over_threshold("aabbccdd") == "aabbccdd"