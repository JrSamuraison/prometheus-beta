"""
LZVN Compression Algorithm Implementation

This module provides a basic implementation of the LZVN (Lempel-Ziv Variable-Length Null-suppressing) 
compression algorithm used in Apple's compression library.

The implementation focuses on the core principles of LZ compression with variable-length encoding.
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
        # Look for repeated sequences
        match_length = 0
        match_offset = 0
        
        # Simple matching strategy
        for look_behind in range(1, min(index + 1, 256)):
            current_match_length = 0
            while (index + current_match_length < len(data) and 
                   data[index + current_match_length] == data[index - look_behind + current_match_length] and 
                   current_match_length < 15):
                current_match_length += 1
            
            if current_match_length > match_length:
                match_length = current_match_length
                match_offset = look_behind
        
        # Encoding logic
        if match_length > 2:
            # Compressed token: offset | length
            token = ((match_offset & 0x0F) << 4) | (match_length & 0x0F)
            compressed.append(token)
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
        token = compressed_data[index]
        
        # Determine if token represents a match or literal
        match_offset = (token >> 4) & 0x0F
        match_length = token & 0x0F
        
        if match_length == 0 and match_offset == 0:
            # Literal byte
            decompressed.append(compressed_data[index])
            index += 1
        elif match_length > 0:
            # Repeated sequence
            if len(decompressed) < match_offset:
                raise ValueError("Corrupted compressed data")
            
            start = len(decompressed) - match_offset
            for i in range(match_length):
                decompressed.append(decompressed[start + i])
            
            index += 1
        else:
            # Invalid token
            raise ValueError("Invalid compression token")
    
    return bytes(decompressed)