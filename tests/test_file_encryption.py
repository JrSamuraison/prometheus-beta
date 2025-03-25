import os
import pytest
import tempfile
from cryptography.fernet import Fernet
from src.file_encryption import encrypt_file, generate_key

def test_generate_key():
    # Test key generation
    key = generate_key()
    assert isinstance(key, bytes)
    assert len(key) > 0

def test_encrypt_file_with_default_options():
    # Create a temporary file with test content
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        original_content = b"Secret test data"
        temp_input.write(original_content)
        input_path = temp_input.name
    
    try:
        # Encrypt the file
        encryption_key = encrypt_file(input_path)
        encrypted_path = input_path + '.encrypted'
        
        # Verify files
        assert os.path.exists(encrypted_path)
        
        # Read and decrypt
        fernet = Fernet(encryption_key)
        with open(encrypted_path, 'rb') as encrypted_file:
            decrypted_content = fernet.decrypt(encrypted_file.read())
        
        assert decrypted_content == original_content
    
    finally:
        # Clean up
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(encrypted_path):
            os.unlink(encrypted_path)

def test_encrypt_file_with_custom_paths():
    # Create a temporary file with test content
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        original_content = b"Another secret test data"
        temp_input.write(original_content)
        input_path = temp_input.name
    
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_output:
        output_path = temp_output.name
    
    try:
        # Encrypt the file
        key = generate_key()
        encrypt_file(input_path, output_path, key)
        
        # Verify files
        assert os.path.exists(output_path)
        
        # Read and decrypt
        fernet = Fernet(key)
        with open(output_path, 'rb') as encrypted_file:
            decrypted_content = fernet.decrypt(encrypted_file.read())
        
        assert decrypted_content == original_content
    
    finally:
        # Clean up
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(output_path):
            os.unlink(output_path)

def test_encrypt_file_error_handling():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        encrypt_file('/path/to/nonexistent/file')
    
    # Test invalid input path
    with pytest.raises(ValueError):
        encrypt_file(None)