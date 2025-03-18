import os
import pytest
import tempfile
import shutil

from src.file_renamer import rename_file

def test_successful_file_rename():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a source file
        source_path = os.path.join(temp_dir, 'source.txt')
        destination_path = os.path.join(temp_dir, 'destination.txt')
        
        with open(source_path, 'w') as f:
            f.write('Test content')
        
        # Rename the file
        result = rename_file(source_path, destination_path)
        
        # Verify file is renamed
        assert result == destination_path
        assert os.path.exists(destination_path)
        assert not os.path.exists(source_path)

def test_nonexistent_source_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'nonexistent.txt')
        destination_path = os.path.join(temp_dir, 'destination.txt')
        
        with pytest.raises(FileNotFoundError):
            rename_file(source_path, destination_path)

def test_destination_file_exists():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'source.txt')
        destination_path = os.path.join(temp_dir, 'destination.txt')
        
        # Create both source and destination files
        with open(source_path, 'w') as f:
            f.write('Source content')
        with open(destination_path, 'w') as f:
            f.write('Destination content')
        
        with pytest.raises(FileExistsError):
            rename_file(source_path, destination_path)

def test_rename_directory_fails():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_dir = os.path.join(temp_dir, 'source_dir')
        destination_dir = os.path.join(temp_dir, 'destination_dir')
        
        os.makedirs(source_dir)
        
        with pytest.raises(IsADirectoryError):
            rename_file(source_dir, destination_dir)

def test_invalid_input_types():
    with pytest.raises(TypeError):
        rename_file(123, 'destination')
    
    with pytest.raises(TypeError):
        rename_file('source', 456)

def test_rename_to_nested_directory():
    # Test renaming a file to a nested directory that doesn't exist
    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = os.path.join(temp_dir, 'source.txt')
        destination_path = os.path.join(temp_dir, 'nested', 'subdirectory', 'destination.txt')
        
        with open(source_path, 'w') as f:
            f.write('Test content')
        
        result = rename_file(source_path, destination_path)
        
        assert result == destination_path
        assert os.path.exists(destination_path)
        assert not os.path.exists(source_path)