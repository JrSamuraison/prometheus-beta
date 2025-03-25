import zlib
import typing

def compress_data(data: typing.Union[str, bytes], compression_level: int = 6) -> bytes:
    """
    Compress input data using Zlib compression algorithm.

    Args:
        data (str or bytes): The input data to compress. 
                              If str, it will be encoded to bytes first.
        compression_level (int, optional): Compression level from 0-9. 
                                           Defaults to 6 (default zlib compression).
                                           0 = no compression, 9 = max compression.

    Returns:
        bytes: Compressed data.

    Raises:
        ValueError: If compression level is not between 0 and 9.
        TypeError: If input data is not str or bytes.
    """
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Convert str to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes")

    # Compress data using zlib
    try:
        compressed_data = zlib.compress(data, compression_level)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_data(compressed_data: bytes) -> bytes:
    """
    Decompress Zlib-compressed data.

    Args:
        compressed_data (bytes): The compressed data to decompress.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        zlib.error: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Decompress data using zlib
    try:
        decompressed_data = zlib.decompress(compressed_data)
        return decompressed_data
    except zlib.error as e:
        raise zlib.error(f"Decompression failed: {str(e)}")