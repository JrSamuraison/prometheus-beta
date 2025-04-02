import os
import hashlib

def are_files_identical(file1_path: str, file2_path: str) -> bool:
    """
    Compare two files to check if they are identical.

    Args:
        file1_path (str): Path to the first file
        file2_path (str): Path to the second file

    Returns:
        bool: True if files are identical, False otherwise

    Raises:
        FileNotFoundError: If either file does not exist
        PermissionError: If there are permission issues reading the files
    """
    # Check if files exist
    if not os.path.exists(file1_path):
        raise FileNotFoundError(f"File not found: {file1_path}")
    if not os.path.exists(file2_path):
        raise FileNotFoundError(f"File not found: {file2_path}")

    # Check file sizes first (quick initial comparison)
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False

    # Compute and compare file hashes for precise comparison
    def compute_file_hash(filepath):
        """Compute SHA-256 hash of a file."""
        hash_sha256 = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()

    try:
        return compute_file_hash(file1_path) == compute_file_hash(file2_path)
    except PermissionError:
        raise PermissionError(f"Permission denied when reading files: {file1_path}, {file2_path}")