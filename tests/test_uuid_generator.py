import re
import pytest
from src.uuid_generator import generate_uuid

def test_uuid_generation():
    """
    Test that generate_uuid() produces a valid UUID v4 string
    """
    # Generate a UUID
    uuid = generate_uuid()
    
    # Check UUID format using regex for v4 UUID
    uuid_pattern = re.compile(
        r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', 
        re.IGNORECASE
    )
    
    # Assertions
    assert isinstance(uuid, str), "UUID should be a string"
    assert len(uuid) == 36, "UUID should be 36 characters long"
    assert uuid_pattern.match(uuid) is not None, "UUID does not match v4 format"

def test_uuid_uniqueness():
    """
    Test that multiple UUID generations produce unique results
    """
    # Generate multiple UUIDs
    uuids = set(generate_uuid() for _ in range(1000))
    
    # Check that all generated UUIDs are unique
    assert len(uuids) == 1000, "UUIDs should be unique"

def test_uuid_version():
    """
    Verify that the generated UUID has the correct version (4)
    """
    uuid = generate_uuid()
    
    # Check version bit (4th character of 3rd segment should be 4)
    assert uuid.split('-')[2][0] == '4', "UUID version should be 4"

def test_uuid_variant():
    """
    Verify that the generated UUID has the correct variant (1)
    """
    uuid = generate_uuid()
    
    # Check variant bits (first character of 4th segment should be 8, 9, a, or b)
    assert uuid.split('-')[3][0] in '89ab', "UUID variant should be 1"