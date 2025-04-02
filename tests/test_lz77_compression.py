import pytest
from src.lz77_compression import lz77_compress, lz77_decompress

def test_lz77_basic_compression():
    """Test basic compression and decompression"""
    original = b"AAAAABBBBB"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed == original

def test_lz77_repeated_pattern():
    """Test compression with repeated patterns"""
    original = b"ABCABCABCABC"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed == original

def test_lz77_empty_input():
    """Test compression and decompression of empty input"""
    original = b""
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed == original

def test_lz77_single_character():
    """Test compression of a single character"""
    original = b"A"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed == original

def test_lz77_complex_pattern():
    """Test compression with more complex pattern"""
    original = b"Hello, hello, hello world!"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed == original

def test_lz77_mixed_characters():
    """Test compression with mixed characters"""
    original = b"abcdefghijklmnopqrstuvwxyz"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed == original

def test_lz77_string_input():
    """Test compression with string input"""
    original = "Hello, world!"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed == original.encode('utf-8')

def test_compression_decompression_consistency():
    """Ensure multiple compression and decompression cycles work"""
    original = b"test data with some repetition test data test data"
    compressed = lz77_compress(original)
    decompressed = lz77_decompress(compressed)
    assert decompressed == original

    # Compress decompressed data again
    recompressed = lz77_compress(decompressed)
    rederived = lz77_decompress(recompressed)
    assert rederived == original