import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file to the specified mode.

    Args:
        file_path (str): The path to the file whose permissions are to be changed.
        mode (int): The new file permissions as an octal number (e.g., 0o755).

    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If file_path is not a string or mode is not an integer.
        ValueError: If the mode is not a valid permission value.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer")
    
    # Validate file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")
    
    # Validate mode is a valid permission value
    if mode < 0 or mode > 0o777:
        raise ValueError("Mode must be between 0 and 0o777")
    
    try:
        # Change file permissions
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"No permission to change mode of {file_path}")
    
    # Verify the permissions were changed
    current_mode = os.stat(file_path).st_mode & 0o777
    if current_mode != mode:
        raise RuntimeError(f"Failed to set permissions to {oct(mode)}")
    
    return True