import os
import time
import random

def generate_uuid() -> str:
    """
    Generate a version 4 UUID (Universally Unique Identifier) without using external libraries.
    
    This implementation creates a UUID by combining:
    - Current timestamp
    - Random bytes from os.urandom()
    - Random numbers generated using the random module
    
    Returns:
        str: A UUID v4 formatted string (8-4-4-4-12 hexadecimal segments)
    """
    # Get current timestamp and random bytes
    timestamp = int(time.time() * 1000)
    random_bytes = os.urandom(10)
    
    # Generate random components
    time_low = timestamp & 0xFFFFFFFF
    time_mid = (timestamp >> 32) & 0xFFFF
    time_hi_version = ((timestamp >> 48) & 0x0FFF) | (4 << 12)  # Version 4
    
    # Create random clock sequence and node components
    clock_seq = random.randint(0, 0x3FFF)
    clock_seq_low = clock_seq & 0xFF
    clock_seq_hi_variant = ((clock_seq >> 8) & 0x3F) | 0x80  # Variant 1
    
    # Combine random and timestamp components
    node = int.from_bytes(random_bytes, byteorder='big') & ((1 << 48) - 1)
    
    # Format the UUID
    uuid_parts = [
        f"{time_low:08x}",
        f"{time_mid:04x}",
        f"{time_hi_version:04x}",
        f"{clock_seq_hi_variant:02x}{clock_seq_low:02x}",
        f"{node:012x}"
    ]
    
    return "-".join(uuid_parts)