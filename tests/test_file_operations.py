import os
import pytest
import tempfile
import shutil

from src.file_operations import delete_file

def test_delete_file_success():
    """Test successful file deletion"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write(b"Test content")
        temp_file.close()
        
        assert os.path.exists(temp_path)
        assert delete_file(temp_path) == True
        assert not os.path.exists(temp_path)

def test_delete_nonexistent_file():
    """Test deleting a file that does not exist"""
    with pytest.raises(FileNotFoundError):
        delete_file("/path/to/nonexistent/file.txt")

def test_delete_directory():
    """Test attempting to delete a directory"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(IsADirectoryError):
            delete_file(temp_dir)

def test_delete_file_with_special_characters():
    """Test deleting a file with special characters in its name"""
    with tempfile.NamedTemporaryFile(prefix="test_file@#$%^", delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write(b"Test content")
        temp_file.close()
        
        assert os.path.exists(temp_path)
        assert delete_file(temp_path) == True
        assert not os.path.exists(temp_path)

def test_delete_readonly_file():
    """Test deleting a read-only file"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write(b"Test content")
        temp_file.close()
        
        # Make the file read-only for current user
        os.chmod(temp_path, 0o400)
        
        try:
            with pytest.raises(PermissionError):
                delete_file(temp_path)
        finally:
            # Restore permissions to allow cleanup
            os.chmod(temp_path, 0o666)
            if os.path.exists(temp_path):
                os.unlink(temp_path)