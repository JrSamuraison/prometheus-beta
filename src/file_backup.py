import os
import shutil
from datetime import datetime

def create_file_backup(file_path, backup_dir=None):
    """
    Create a backup of a given file with a timestamp.

    Args:
        file_path (str): Path to the file to be backed up.
        backup_dir (str, optional): Directory to store backups. 
                                    If None, backup in same directory as source file.

    Returns:
        str: Path to the created backup file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        IsADirectoryError: If the source path is a directory, not a file.
        PermissionError: If there are insufficient permissions to read/write files.
    """
    # Validate input file exists and is a file
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found: {file_path}")
    
    if not os.path.isfile(file_path):
        raise IsADirectoryError(f"Source path is not a file: {file_path}")

    # Determine backup directory
    if backup_dir is None:
        backup_dir = os.path.dirname(file_path) or '.'

    # Create backup directory if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)

    # Generate backup filename with timestamp
    filename = os.path.basename(file_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{filename}.{timestamp}.bak"
    backup_path = os.path.join(backup_dir, backup_filename)

    # Copy file to backup location
    try:
        shutil.copy2(file_path, backup_path)
    except PermissionError:
        raise PermissionError(f"Permission denied when creating backup of {file_path}")

    return backup_path