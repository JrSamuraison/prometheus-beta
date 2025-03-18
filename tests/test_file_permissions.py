import os
import pytest
import tempfile
from src.file_permissions import change_file_permissions

def test_change_file_permissions_normal_case():
    # Create a temp file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Test changing to read and write for owner
    change_file_permissions(temp_path, 0o600)
    mode = os.stat(temp_path).st_mode
    assert (mode & 0o777) == 0o600
    
    # Cleanup
    os.unlink(temp_path)

def test_change_file_permissions_full_permissions():
    # Create a temp file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Test changing to full permissions
    change_file_permissions(temp_path, 0o777)
    mode = os.stat(temp_path).st_mode
    assert (mode & 0o777) == 0o777
    
    # Cleanup
    os.unlink(temp_path)

def test_change_file_permissions_no_write():
    # Create a temp file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Test changing to read-only
    change_file_permissions(temp_path, 0o444)
    mode = os.stat(temp_path).st_mode
    assert (mode & 0o777) == 0o444
    
    # Cleanup
    os.unlink(temp_path)

def test_change_file_permissions_invalid_file():
    with pytest.raises(FileNotFoundError):
        change_file_permissions("/path/to/nonexistent/file", 0o755)

def test_change_file_permissions_invalid_mode():
    # Create a temp file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    with pytest.raises(ValueError):
        change_file_permissions(temp_path, 0o1000)  # Out of valid range
    
    # Cleanup
    os.unlink(temp_path)

def test_change_file_permissions_invalid_input_types():
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o755)  # Invalid file path type
    
    with pytest.raises(TypeError):
        change_file_permissions("/path/to/file", "755")  # Invalid mode type