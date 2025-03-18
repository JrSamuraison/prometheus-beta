import pytest
from src.aho_corasick import AhoCorasick

def test_basic_matching():
    """
    Test basic pattern matching with simple strings
    """
    patterns = ['he', 'she', 'his', 'hers']
    text = "ushers"
    
    ac = AhoCorasick(patterns)
    matches = ac.find_matches(text)
    
    # Expected matches: ('he' at index 1), ('she' at index 2), ('hers' at index 2)
    expected_matches = [
        (1, 'he'), 
        (2, 'she'), 
        (2, 'hers')
    ]
    
    assert sorted(matches) == sorted(expected_matches)

def test_overlapping_matches():
    """
    Test matching of overlapping patterns
    """
    patterns = ['ab', 'abc', 'bc']
    text = "abcdef"
    
    ac = AhoCorasick(patterns)
    matches = ac.find_matches(text)
    
    expected_matches = [
        (0, 'ab'), 
        (0, 'abc'), 
        (1, 'bc')
    ]
    
    assert sorted(matches) == sorted(expected_matches)

def test_no_matches():
    """
    Test scenario with no pattern matches
    """
    patterns = ['abc', 'def']
    text = "ghijkl"
    
    ac = AhoCorasick(patterns)
    matches = ac.find_matches(text)
    
    assert matches == []

def test_multiple_occurrences():
    """
    Test multiple occurrences of the same pattern
    """
    patterns = ['ab']
    text = "abababab"
    
    ac = AhoCorasick(patterns)
    matches = ac.find_matches(text)
    
    expected_matches = [
        (0, 'ab'), 
        (2, 'ab'), 
        (4, 'ab'), 
        (6, 'ab')
    ]
    
    assert sorted(matches) == sorted(expected_matches)

def test_empty_inputs():
    """
    Test handling of empty inputs
    """
    # Empty patterns list
    with pytest.raises(TypeError):
        AhoCorasick()
    
    # Empty text
    patterns = ['test']
    ac = AhoCorasick(patterns)
    matches = ac.find_matches("")
    assert matches == []

def test_case_sensitivity():
    """
    Test case sensitivity of matching
    """
    patterns = ['Hello', 'World']
    text = "hello world HELLO WORLD"
    
    ac = AhoCorasick(patterns)
    matches = ac.find_matches(text)
    
    # Exact case matches only
    assert matches == []

def test_long_text_with_multiple_patterns():
    """
    Test matching in a longer text with multiple patterns
    """
    patterns = ['car', 'carpet', 'java', 'javascript']
    text = "I love programming in javascript and driving a car with a carpet"
    
    ac = AhoCorasick(patterns)
    matches = ac.find_matches(text)
    
    expected_matches = [
        (38, 'car'), 
        (38, 'carpet'), 
        (4, 'java'), 
        (4, 'javascript')
    ]
    
    assert sorted(matches) == sorted(expected_matches)