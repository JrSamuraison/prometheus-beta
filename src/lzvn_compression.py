"""
LZVN Compression Algorithm Implementation

This module provides a basic implementation of the LZVN (Lempel-Ziv Variable-Length Null-suppressing) 
compression algorithm used in Apple's compression library.

The implementation focuses on simple LZ-style compression with minimal overhead.
"""

def lzvn_compress(data):
    """
    Compress input data using a basic LZVN-inspired compression algorithm.

    Args:
        data (bytes): The input data to be compressed.

    Returns:
        bytes: Compressed data.

    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
    """
    # Input validation
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")

    # Compression buffers
    compressed = bytearray()
    index = 0
    
    while index < len(data):
        # Look for adjacent repeated bytes
        match_length = 1
        while (index + match_length < len(data) and 
               data[index] == data[index + match_length] and 
               match_length < 15):
            match_length += 1
        
        if match_length > 1:
            # Encode repeated bytes
            token = (0 << 4) | (match_length & 0x0F)
            compressed.append(token)
            compressed.append(data[index])
            index += match_length
        else:
            # Literal byte
            compressed.append(data[index])
            index += 1
    
    return bytes(compressed)

def lzvn_decompress(compressed_data):
    """
    Decompress data that was compressed using the LZVN-inspired algorithm.

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

    # Decompression buffers
    decompressed = bytearray()
    index = 0
    
    while index < len(compressed_data):
        # Read token: high 4 bits for special encoding, low 4 bits for length
        token = compressed_data[index]
        match_type = (token >> 4) & 0x0F
        match_length = token & 0x0F
        
        if match_type == 0 and match_length > 1:
            # Repeated byte sequence
            if index + 1 >= len(compressed_data):
                break
            repeat_byte = compressed_data[index + 1]
            for _ in range(match_length):
                decompressed.append(repeat_byte)
            index += 2
        else:
            # Literal byte
            decompressed.append(compressed_data[index])
            index += 1
    
    return bytes(decompressed)