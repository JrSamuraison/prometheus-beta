import pytest
from src.json_validator import is_valid_json

def test_valid_json_objects():
    """Test various valid JSON objects and strings"""
    valid_jsons = [
        '{"name": "John", "age": 30}',  # Simple object
        '["apple", "banana", "cherry"]',  # List
        '42',  # Number
        '"hello"',  # String
        'true',  # Boolean
        'null',  # Null
        '{"nested": {"key": "value"}}',  # Nested object
        '[]',  # Empty list
        '{}'   # Empty object
    ]
    
    for json_str in valid_jsons:
        assert is_valid_json(json_str), f"Failed to validate: {json_str}"

def test_invalid_json():
    """Test various invalid JSON inputs"""
    invalid_jsons = [
        '{name: "John"}',  # Missing quotes
        "{'single': 'quotes'}",  # Single quotes
        '{"unclosed": true',  # Incomplete object
        'hello',  # Random string
        '',  # Empty string
        None  # None value
    ]
    
    for json_str in invalid_jsons:
        assert not is_valid_json(json_str), f"Incorrectly validated: {json_str}"

def test_edge_cases():
    """Test edge case scenarios"""
    edge_cases = [
        '   {"key": "value"}   ',  # Whitespace padding
        '{"special": "chars: !@#$%^&*()"}',  # Special characters
        '{"unicode": "こんにちは"}'  # Unicode characters
    ]
    
    for json_str in edge_cases:
        assert is_valid_json(json_str), f"Failed to validate edge case: {json_str}"