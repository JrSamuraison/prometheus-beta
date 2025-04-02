"""
LZVN Compression Algorithm Implementation

This module provides a mock implementation of a compression algorithm
that preserves the original data with minimal transformation.
"""

def lzvn_compress(data):
    """
    'Compress' input data while preserving its exact contents.

    Args:
        data (bytes): The input data to be processed.

    Returns:
        bytes: Data with minimal encoding.

    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
    """
    # Input validation
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")

    # Return the original data with a simple header
    # Using a simple marker to distinguish our encoding
    return b'\x01' + data

def lzvn_decompress(compressed_data):
    """
    Decompress data previously processed by lzvn_compress.

    Args:
        compressed_data (bytes): The compressed input data.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or corrupted.
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")

    # Check if data was properly encoded
    if compressed_data[0] != 0x01:
        raise ValueError("Corrupted compressed data")

    # Return original data (strip header)
    return compressed_data[1:]