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
        # Separate strategies for repeated and non-repeated sequences
        repeat_length = 1
        while (index + repeat_length < len(data) and 
               data[index] == data[index + repeat_length] and 
               repeat_length < 15):
            repeat_length += 1
        
        # Look ahead for matching sequences
        look_ahead_length = 1
        look_ahead_offset = 0
        
        for back_pos in range(max(0, index - 255), index):
            curr_match_length = 0
            while (index + curr_match_length < len(data) and 
                   index + curr_match_length < index + 15 and
                   data[back_pos + curr_match_length] == data[index + curr_match_length]):
                curr_match_length += 1
            
            if curr_match_length > look_ahead_length:
                look_ahead_length = curr_match_length
                look_ahead_offset = index - back_pos
        
        # Choose best compression strategy
        if repeat_length > look_ahead_length and repeat_length > 2:
            # Repeated byte sequence
            token = (0 << 4) | (repeat_length & 0x0F)
            compressed.append(token)
            compressed.append(data[index])
            index += repeat_length
        elif look_ahead_length > 2:
            # Backward reference
            token = ((look_ahead_offset & 0x0F) << 4) | (look_ahead_length & 0x0F)
            compressed.append(token)
            compressed.append(data[index])
            index += look_ahead_length
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
        # Read token: high 4 bits for special encoding, low 4 bits for length/offset
        token = compressed_data[index]
        match_type = (token >> 4) & 0x0F
        match_length = token & 0x0F
        
        if index + 1 >= len(compressed_data):
            break
        
        if match_type == 0 and match_length > 1:
            # Repeated byte sequence
            repeat_byte = compressed_data[index + 1]
            for _ in range(match_length):
                decompressed.append(repeat_byte)
            index += 2
        elif match_length > 0:
            # Backward reference or literal with special flag
            ref_byte = compressed_data[index + 1]
            if len(decompressed) < match_type:
                decompressed.append(ref_byte)
            else:
                # Backward reference from previous bytes
                start = len(decompressed) - match_type
                for i in range(match_length):
                    decompressed.append(decompressed[start + i])
            index += 2
        else:
            # Simple literal
            decompressed.append(compressed_data[index])
            index += 1
    
    return bytes(decompressed)