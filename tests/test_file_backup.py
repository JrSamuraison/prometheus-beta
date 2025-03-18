import os
import pytest
import tempfile
import shutil
from src.file_backup import create_file_backup

def test_create_file_backup_same_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("Test content")
        temp_file_path = temp_file.name

    try:
        # Create backup
        backup_path = create_file_backup(temp_file_path)

        # Check backup was created
        assert os.path.exists(backup_path)
        assert os.path.basename(temp_file_path) in os.path.basename(backup_path)
        assert backup_path.endswith('.bak')

        # Check backup content matches original
        with open(temp_file_path, 'r') as orig, open(backup_path, 'r') as backup:
            assert orig.read() == backup.read()
    finally:
        # Clean up
        os.unlink(temp_file_path)
        os.unlink(backup_path)

def test_create_file_backup_custom_directory():
    # Create temporary files and directories
    with tempfile.TemporaryDirectory() as temp_dir:
        with tempfile.NamedTemporaryFile(delete=False, mode='w', dir=temp_dir) as temp_file:
            temp_file.write("Test content")
            temp_file_path = temp_file.name

        backup_dir = os.path.join(temp_dir, 'backups')

        try:
            # Create backup in custom directory
            backup_path = create_file_backup(temp_file_path, backup_dir)

            # Check backup was created in specified directory
            assert os.path.exists(backup_path)
            assert os.path.dirname(backup_path) == backup_dir
            assert os.path.basename(temp_file_path) in os.path.basename(backup_path)
            assert backup_path.endswith('.bak')

            # Check backup content matches original
            with open(temp_file_path, 'r') as orig, open(backup_path, 'r') as backup:
                assert orig.read() == backup.read()
        finally:
            # Clean up is handled by tempfile and tempdir contexts

def test_create_file_backup_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        create_file_backup('/path/to/nonexistent/file.txt')

def test_create_file_backup_directory_input():
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(IsADirectoryError):
            create_file_backup(temp_dir)