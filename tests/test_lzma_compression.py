import pytest
import lzma
from src.lzma_compression import lzma_compress, lzma_decompress

def test_lzma_compression_basic():
    """Test basic compression and decompression"""
    original_data = "Hello, world! This is a test of LZMA compression."
    compressed = lzma_compress(original_data)
    
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original_data.encode('utf-8'))
    
    decompressed = lzma_decompress(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_lzma_compression_binary():
    """Test compression with binary data"""
    original_data = b'\x00\x01\x02\x03\x04\x05\x06\x07'
    compressed = lzma_compress(original_data)
    
    assert isinstance(compressed, bytes)
    
    decompressed = lzma_decompress(compressed)
    assert decompressed == original_data

def test_lzma_compression_levels():
    """Test different compression levels"""
    original_data = "Test data for compression levels" * 100
    
    for level in range(10):
        compressed = lzma_compress(original_data, compression_level=level)
        decompressed = lzma_decompress(compressed)
        assert decompressed.decode('utf-8') == original_data

def test_lzma_compression_empty_input():
    """Test compression with empty input"""
    original_data = ""
    compressed = lzma_compress(original_data)
    decompressed = lzma_decompress(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_lzma_compression_invalid_input_type():
    """Test compression with invalid input type"""
    with pytest.raises(TypeError):
        lzma_compress(123)
    
    with pytest.raises(TypeError):
        lzma_decompress("not bytes")

def test_lzma_compression_invalid_compression_level():
    """Test compression with invalid compression level"""
    with pytest.raises(ValueError):
        lzma_compress("test", compression_level=-1)
    
    with pytest.raises(ValueError):
        lzma_compress("test", compression_level=10)

def test_lzma_decompress_invalid_data():
    """Test decompression with invalid compressed data"""
    with pytest.raises(lzma.LZMAError):
        lzma_decompress(b'Invalid compressed data')