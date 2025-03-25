import os
import pytest
import tempfile
import time
from src.oldest_file import find_oldest_file

def test_find_oldest_file_basic():
    """Test finding the oldest file in a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple files with different creation times
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        # Ensure time difference between file creations
        with open(file1_path, 'w') as f:
            f.write('test1')
        
        time.sleep(0.1)  # Small delay to ensure different creation times
        
        with open(file2_path, 'w') as f:
            f.write('test2')
        
        # Find the oldest file
        oldest = find_oldest_file(temp_dir)
        
        # The first created file should be the oldest
        assert oldest == file1_path

def test_empty_directory():
    """Test behavior with an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert find_oldest_file(temp_dir) is None

def test_nonexistent_directory():
    """Test behavior with a nonexistent directory."""
    assert find_oldest_file('/path/to/nonexistent/directory') is None

def test_file_instead_of_directory():
    """Test behavior when a file path is provided instead of a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert find_oldest_file(temp_file.name) is None

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        find_oldest_file(123)
    
    with pytest.raises(ValueError):
        find_oldest_file('')

def test_permission_denied(monkeypatch):
    """Test handling of permission-denied scenarios."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Simulate a permission error
        def mock_listdir(*args, **kwargs):
            raise PermissionError("Simulated permission error")
        
        monkeypatch.setattr(os, 'listdir', mock_listdir)
        
        assert find_oldest_file(temp_dir) is None