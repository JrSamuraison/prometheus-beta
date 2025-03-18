import os
import shutil

def rename_file(source_path, destination_path):
    """
    Rename a file from source path to destination path.

    Args:
        source_path (str): The current path of the file to be renamed.
        destination_path (str): The new path for the file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are insufficient permissions to rename the file.
        IsADirectoryError: If the source path is a directory.
        FileExistsError: If the destination file already exists.
    """
    # Validate input paths are strings
    if not isinstance(source_path, str) or not isinstance(destination_path, str):
        raise TypeError("Source and destination paths must be strings")

    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")

    # Check if source is a file, not a directory
    if os.path.isdir(source_path):
        raise IsADirectoryError(f"Source path is a directory: {source_path}")

    # Check if destination file already exists
    if os.path.exists(destination_path):
        raise FileExistsError(f"Destination file already exists: {destination_path}")

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    try:
        # Rename the file
        shutil.move(source_path, destination_path)
    except PermissionError:
        raise PermissionError(f"Permission denied when renaming file: {source_path}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error renaming file: {e}")

    return destination_path