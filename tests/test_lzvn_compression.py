"""
Test suite for LZVN Compression Algorithm
"""

import pytest
from src.lzvn_compression import lzvn_compress, lzvn_decompress

def test_basic_compression():
    """Test basic compression and decompression"""
    original_data = b"Hello, world! This is a test of LZVN compression."
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_repeated_data_compression():
    """Test compression of highly repetitive data"""
    original_data = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_binary_data_compression():
    """Test compression of binary data"""
    original_data = bytes([0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7])
    compressed = lzvn_compress(original_data)
    decompressed = lzvn_decompress(compressed)
    
    assert decompressed == original_data

def test_edge_cases():
    """Test edge cases for compression"""
    # Single byte
    single_byte = b"A"
    assert lzvn_decompress(lzvn_compress(single_byte)) == single_byte

    # Multiple single bytes
    multi_byte = b"ABCDEFGHIJKLMNOP"
    assert lzvn_decompress(lzvn_compress(multi_byte)) == multi_byte

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Invalid input type
    with pytest.raises(TypeError):
        lzvn_compress("Not bytes")
    
    with pytest.raises(TypeError):
        lzvn_decompress("Not bytes")
    
    # Empty input
    with pytest.raises(ValueError):
        lzvn_compress(b"")
    
    with pytest.raises(ValueError):
        lzvn_decompress(b"")