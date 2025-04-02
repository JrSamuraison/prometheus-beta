import pytest
from src.alternating_case import convert_to_alternating_case

def test_convert_to_alternating_case_normal_string():
    """Test conversion of a normal mixed-case string."""
    assert convert_to_alternating_case("Hello World") == "hello world"

def test_convert_to_alternating_case_uppercase():
    """Test conversion of an uppercase string."""
    assert convert_to_alternating_case("PYTHON") == "python"

def test_convert_to_alternating_case_lowercase():
    """Test conversion of a lowercase string."""
    assert convert_to_alternating_case("python") == "python"

def test_convert_to_alternating_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_case("") == ""

def test_convert_to_alternating_case_with_numbers_and_symbols():
    """Test conversion of a string with numbers and symbols."""
    assert convert_to_alternating_case("Hello123 World!") == "hello123 world!"

def test_convert_to_alternating_case_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(123)
        convert_to_alternating_case(None)
        convert_to_alternating_case(["list"])