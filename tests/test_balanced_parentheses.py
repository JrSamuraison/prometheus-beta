import pytest
from src.balanced_parentheses import is_balanced_parentheses

def test_basic_balanced_cases():
    """Test basic balanced parentheses scenarios."""
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("(())") == True
    assert is_balanced_parentheses("()()") == True

def test_unbalanced_cases():
    """Test unbalanced parentheses scenarios."""
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses(")(") == False
    assert is_balanced_parentheses("((()") == False
    assert is_balanced_parentheses("())") == False

def test_empty_and_non_parenthesis_strings():
    """Test edge cases like empty string and strings with other characters."""
    assert is_balanced_parentheses("") == True
    assert is_balanced_parentheses("hello") == True
    assert is_balanced_parentheses("hello()world") == True
    assert is_balanced_parentheses("(hello)") == True

def test_complex_nested_cases():
    """Test more complex nested parentheses scenarios."""
    assert is_balanced_parentheses("((()))") == True
    assert is_balanced_parentheses("(()())") == True
    assert is_balanced_parentheses("(()())(()())") == True

def test_multiple_unbalanced_scenarios():
    """Test multiple complex unbalanced scenarios."""
    assert is_balanced_parentheses("((()") == False
    assert is_balanced_parentheses("())()") == False
    assert is_balanced_parentheses("(()())(()") == False