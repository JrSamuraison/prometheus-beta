import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_str_data():
    """Test compression with string input"""
    original = "Hello, world! This is a test of Zlib compression."
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original.encode('utf-8'))

def test_compress_bytes_data():
    """Test compression with bytes input"""
    original = b"Binary data compression test"
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original)

def test_compression_levels():
    """Test different compression levels"""
    data = "Test compression levels" * 100  # Create larger data
    
    # Test min, mid, and max compression levels
    compressed_min = compress_data(data, compression_level=0)
    compressed_mid = compress_data(data, compression_level=6)
    compressed_max = compress_data(data, compression_level=9)
    
    # Verify different levels result in different compressed sizes
    assert len(compressed_min) >= len(compressed_mid)
    assert len(compressed_mid) >= len(compressed_max)

def test_compress_decompress_round_trip():
    """Test full compression and decompression round trip"""
    original = "Zlib compression and decompression test!"
    compressed = compress_data(original)
    decompressed = decompress_data(compressed)
    
    assert decompressed.decode('utf-8') == original

def test_compress_invalid_level():
    """Test handling of invalid compression levels"""
    with pytest.raises(ValueError):
        compress_data("Test", compression_level=-1)
    with pytest.raises(ValueError):
        compress_data("Test", compression_level=10)

def test_compress_invalid_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    with pytest.raises(TypeError):
        compress_data(None)

def test_decompress_invalid_type():
    """Test handling of invalid decompression input"""
    with pytest.raises(TypeError):
        decompress_data("Not bytes")
    with pytest.raises(TypeError):
        decompress_data(123)

def test_decompress_corrupt_data():
    """Test handling of corrupt compressed data"""
    with pytest.raises(zlib.error):
        decompress_data(b'Corrupt data')

def test_empty_data():
    """Test compression and decompression of empty data"""
    empty_str = ""
    empty_bytes = b""
    
    # Compression
    compressed_str = compress_data(empty_str)
    compressed_bytes = compress_data(empty_bytes)
    
    # Decompression
    assert decompress_data(compressed_str) == b""
    assert decompress_data(compressed_bytes) == b""