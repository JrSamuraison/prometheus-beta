import os
from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a new encryption key.
    
    Returns:
        bytes: A new Fernet encryption key
    """
    return Fernet.generate_key()

def encrypt_file(input_path, output_path=None, key=None):
    """
    Encrypt the contents of a file using Fernet symmetric encryption.
    
    Args:
        input_path (str): Path to the input file to be encrypted
        output_path (str, optional): Path to save the encrypted file. 
            If None, appends '.encrypted' to the input file name.
        key (bytes, optional): Encryption key. If None, a new key is generated.
    
    Returns:
        bytes: The encryption key used
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
        ValueError: If input path is invalid
    """
    # Validate input path
    if not input_path or not isinstance(input_path, str):
        raise ValueError("Invalid input path")
    
    # Check if input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Generate or use provided key
    if key is None:
        key = generate_key()
    
    # Create Fernet cipher
    fernet = Fernet(key)
    
    # Determine output path
    if output_path is None:
        output_path = input_path + '.encrypted'
    
    try:
        # Read input file
        with open(input_path, 'rb') as file:
            file_data = file.read()
        
        # Encrypt data
        encrypted_data = fernet.encrypt(file_data)
        
        # Write encrypted data
        with open(output_path, 'wb') as file:
            file.write(encrypted_data)
        
        return key
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_path}, {output_path}")