def lz77_compress(input_data):
    """
    Implement LZ77 compression algorithm.
    
    Args:
        input_data (str or bytes): The input data to compress
    
    Returns:
        list: A list of tuples representing compressed data 
              Each tuple is (offset, length, next_char)
    """
    # Ensure input is bytes for consistent processing
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate input
    if not input_data:
        return []
    
    # Compression parameters
    window_size = 1024  # Lookback window size
    buffer_size = 16    # Look-ahead buffer size
    
    compressed = []
    current_pos = 0
    
    while current_pos < len(input_data):
        # Find the longest matching sequence
        best_length = 0
        best_offset = 0
        
        # Search window starts at max of 0 and current position - window size
        search_start = max(0, current_pos - window_size)
        search_end = current_pos
        
        # Look-ahead buffer ends at min of input length and current + buffer size
        lookahead_end = min(len(input_data), current_pos + buffer_size)
        
        # Search for longest match in the window
        for offset in range(search_end - search_start):
            match_length = 0
            
            # Check how long the match continues
            while (match_length < buffer_size and 
                   current_pos + match_length < lookahead_end and
                   input_data[search_start + offset + match_length] == 
                   input_data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = search_end - (search_start + offset)
        
        # If no match found, encode single character
        if best_length == 0:
            compressed.append((0, 0, input_data[current_pos]))
            current_pos += 1
        else:
            # Encode match with next character
            next_char = input_data[current_pos + best_length] if current_pos + best_length < len(input_data) else None
            compressed.append((best_offset, best_length, next_char))
            current_pos += best_length + 1
    
    return compressed

def lz77_decompress(compressed_data):
    """
    Decompress LZ77 compressed data.
    
    Args:
        compressed_data (list): Compressed data as list of tuples
    
    Returns:
        bytes: Decompressed data
    """
    # Validate input
    if not compressed_data:
        return b''
    
    decompressed = bytearray()
    
    for offset, length, next_char in compressed_data:
        # If no match (offset and length are 0), just add the character
        if offset == 0 and length == 0:
            decompressed.append(next_char)
        else:
            # Recreate the matched sequence
            start = len(decompressed) - offset
            for i in range(length):
                decompressed.append(decompressed[start + i])
            
            # Add the next character if it exists
            if next_char is not None:
                decompressed.append(next_char)
    
    return bytes(decompressed)