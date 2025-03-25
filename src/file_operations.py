import os
import logging
import stat

def delete_file(file_path):
    """
    Delete a file from the specified path.

    Args:
        file_path (str): The path to the file to be deleted.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permission to delete the file.
        IsADirectoryError: If the path points to a directory instead of a file.
        OSError: For other OS-related errors during file deletion.

    Returns:
        bool: True if the file was successfully deleted.
    """
    try:
        # Normalize the path to handle relative paths
        normalized_path = os.path.abspath(os.path.expanduser(file_path))
        
        # Check if path exists
        if not os.path.exists(normalized_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Check if it's a file (not a directory)
        if not os.path.isfile(normalized_path):
            raise IsADirectoryError(f"Path is not a file: {file_path}")
        
        # Get file stats
        file_stats = os.stat(normalized_path)
        
        # Check file permissions explicitly
        if not bool(file_stats.st_mode & stat.S_IWUSR):
            raise PermissionError(f"No write permission for file: {file_path}")
        
        # Check directory write permissions
        dir_path = os.path.dirname(normalized_path)
        if not os.access(dir_path, os.W_OK):
            raise PermissionError(f"No write permission for directory: {dir_path}")
        
        # Attempt to delete the file
        os.remove(normalized_path)
        logging.info(f"File deleted successfully: {file_path}")
        return True
    
    except PermissionError:
        logging.error(f"Permission denied when trying to delete: {file_path}")
        raise
    except OSError as e:
        logging.error(f"Error deleting file {file_path}: {e}")
        raise