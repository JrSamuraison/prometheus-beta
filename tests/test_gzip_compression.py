import pytest
import sys
import os

# Ensure src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from gzip_compression import gzip_compress, gzip_decompress

def test_gzip_compress_string():
    """Test compressing a string."""
    input_data = "Hello, World!"
    compressed = gzip_compress(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0

def test_gzip_compress_bytes():
    """Test compressing bytes."""
    input_data = b"Hello, World!"
    compressed = gzip_compress(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0

def test_gzip_decompress():
    """Test decompressing gzipped data."""
    input_data = "Hello, World!"
    compressed = gzip_compress(input_data)
    decompressed = gzip_decompress(compressed)
    assert decompressed.decode('utf-8') == input_data

def test_roundtrip_compression():
    """Test full compression and decompression cycle."""
    test_cases = [
        "Hello, World!",
        "Python is awesome!",
        "12345",
        b"Binary data test",
        "áéíóú Unicode test"
    ]
    
    for test_data in test_cases:
        # Handle both string and bytes input
        input_data = test_data if isinstance(test_data, bytes) else test_data.encode('utf-8')
        
        # Compress
        compressed = gzip_compress(test_data)
        
        # Decompress
        decompressed = gzip_decompress(compressed)
        
        # Compare
        assert decompressed == input_data

def test_compress_empty_input_error():
    """Test error handling for empty input."""
    with pytest.raises(ValueError, match="Input cannot be empty"):
        gzip_compress("")
    
    with pytest.raises(ValueError, match="Input cannot be empty"):
        gzip_compress(b"")

def test_compress_none_input_error():
    """Test error handling for None input."""
    with pytest.raises(ValueError, match="Input cannot be None"):
        gzip_compress(None)

def test_compress_invalid_type_error():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string or bytes"):
        gzip_compress(123)
    
    with pytest.raises(TypeError, match="Input must be a string or bytes"):
        gzip_compress([1, 2, 3])

def test_decompress_empty_input_error():
    """Test error handling for empty input in decompression."""
    with pytest.raises(ValueError, match="Input cannot be empty"):
        gzip_decompress(b"")

def test_decompress_none_input_error():
    """Test error handling for None input in decompression."""
    with pytest.raises(ValueError, match="Input cannot be None"):
        gzip_decompress(None)

def test_decompress_invalid_type_error():
    """Test error handling for invalid input types in decompression."""
    with pytest.raises(TypeError, match="Input must be bytes"):
        gzip_decompress("not bytes")
    
    with pytest.raises(TypeError, match="Input must be bytes"):
        gzip_decompress(123)