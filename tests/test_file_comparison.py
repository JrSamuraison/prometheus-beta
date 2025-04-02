import os
import pytest
import tempfile

from src.file_comparison import are_files_identical

def test_identical_files():
    """Test two files with identical content are recognized as identical."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.write("Hello, world!")
        temp2.write("Hello, world!")
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is True
        finally:
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_different_files():
    """Test files with different content are not identical."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.write("Hello, world!")
        temp2.write("Hello, universe!")
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is False
        finally:
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_empty_files():
    """Test two empty files are identical."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is True
        finally:
            os.unlink(temp1.name)
            os.unlink(temp2.name)

def test_nonexistent_file():
    """Test that FileNotFoundError is raised for nonexistent files."""
    with pytest.raises(FileNotFoundError):
        are_files_identical("nonexistent_file1.txt", "nonexistent_file2.txt")

def test_same_file():
    """Test that a file compared with itself is identical."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
        temp.write("Some content")
        temp.close()
        
        try:
            assert are_files_identical(temp.name, temp.name) is True
        finally:
            os.unlink(temp.name)

def test_files_with_different_sizes():
    """Test files with different sizes are not identical."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp1, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as temp2:
        temp1.write("Short content")
        temp2.write("Much longer content that is different")
        temp1.close()
        temp2.close()
        
        try:
            assert are_files_identical(temp1.name, temp2.name) is False
        finally:
            os.unlink(temp1.name)
            os.unlink(temp2.name)