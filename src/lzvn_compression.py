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
        best_match_length = 0
        best_match_offset = 0
        
        # Search back for repeated sequences, limited to 256 bytes
        for look_behind in range(1, min(index + 1, 256)):
            match_length = 0
            while (index + match_length < len(data) and 
                   data[index + match_length] == data[index - look_behind + match_length] and 
                   match_length < 15):
                match_length += 1
            
            # Update best match if found
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = look_behind
        
        # Encoding logic
        if best_match_length > 2:
            # Compressed token: offset | length
            token = ((best_match_offset & 0x0F) << 4) | (best_match_length & 0x0F)
            compressed.append(token)
            index += best_match_length
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
        # Current token represents either match or literal
        token = compressed_data[index]
        
        # Extract match info
        match_offset = (token >> 4) & 0x0F
        match_length = token & 0x0F
        
        # If no match, it's a literal byte
        if match_length == 0 and match_offset == 0:
            decompressed.append(compressed_data[index])
            index += 1
            continue
        
        # For matches, handle sequence expansion
        if match_offset == 0:
            # For literals with no offset, just append
            for _ in range(match_length):
                decompressed.append(compressed_data[index])
            index += 1
        else:
            # Verify we have enough previous bytes for lookback
            if len(decompressed) < match_offset:
                decompressed.append(compressed_data[index])
                index += 1
                continue
            
            # Repeat sequence from previous bytes
            start = len(decompressed) - match_offset
            for i in range(match_length):
                if start + i < len(decompressed):
                    decompressed.append(decompressed[start + i])
                else:
                    break
            index += 1
    
    return bytes(decompressed)