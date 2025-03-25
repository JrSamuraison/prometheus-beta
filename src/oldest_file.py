import os
from typing import Union, Optional

def find_oldest_file(directory_path: str) -> Optional[str]:
    """
    Find the oldest file in a given directory.

    Args:
        directory_path (str): Path to the directory to search.

    Returns:
        Optional[str]: Path to the oldest file, or None if no files exist or directory is invalid.

    Raises:
        TypeError: If directory_path is not a string.
        ValueError: If directory_path is an empty string.
    """
    # Validate input
    if not isinstance(directory_path, str):
        raise TypeError("Directory path must be a string")
    
    if not directory_path:
        raise ValueError("Directory path cannot be an empty string")

    # Normalize the path and check if it exists
    try:
        normalized_path = os.path.abspath(os.path.normpath(directory_path))
        
        # Check if path exists and is a directory
        if not os.path.exists(normalized_path):
            return None
        
        if not os.path.isdir(normalized_path):
            return None
        
        # Get all files in the directory (excluding subdirectories)
        files = [
            os.path.join(normalized_path, f) 
            for f in os.listdir(normalized_path) 
            if os.path.isfile(os.path.join(normalized_path, f))
        ]
        
        # If no files, return None
        if not files:
            return None
        
        # Find the oldest file based on creation time
        return min(files, key=os.path.getctime)
    
    except (TypeError, ValueError, PermissionError):
        # Handle potential errors in path processing
        return None