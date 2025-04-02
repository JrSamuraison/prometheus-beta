"""
LZVN Compression Algorithm Implementation

This module provides a basic implementation of a simple compression algorithm
inspired by LZVN principles.
"""

def lzvn_compress(data):
    """
    Compress input data using a simple compression algorithm.

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

    # Simple compression
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Look for repeated sequences
        repeat_length = 1
        while (i + repeat_length < len(data) and 
               data[i] == data[i + repeat_length] and 
               repeat_length < 15):
            repeat_length += 1
        
        if repeat_length > 1:
            # Encode repeated sequence
            token = (0 << 4) | (repeat_length & 0x0F)
            compressed.append(token)
            compressed.append(data[i])
            i += repeat_length
        else:
            # Literal byte
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def lzvn_decompress(compressed_data):
    """
    Decompress data that was compressed using the simple algorithm.

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

    # Decompression
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Read token
        token = compressed_data[i]
        match_type = (token >> 4) & 0x0F
        match_length = token & 0x0F
        
        # End of stream safety
        if i + 1 >= len(compressed_data):
            break
        
        if match_type == 0 and match_length > 1:
            # Repeated byte sequence
            repeat_byte = compressed_data[i + 1]
            for _ in range(match_length):
                decompressed.append(repeat_byte)
            i += 2
        else:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return bytes(decompressed)