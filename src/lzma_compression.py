import lzma
import typing

def lzma_compress(data: typing.Union[str, bytes], compression_level: int = 6) -> bytes:
    """
    Compress input data using LZMA compression algorithm.

    Args:
        data (str or bytes): The input data to compress.
        compression_level (int, optional): Compression level from 0-9. 
                                           Defaults to 6 (default LZMA compression).

    Returns:
        bytes: Compressed data.

    Raises:
        TypeError: If input is not str or bytes.
        ValueError: If compression level is out of range.
    """
    # Validate input type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")

    # Validate compression level
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Compress data using LZMA
    compressed_data = lzma.compress(data, preset=compression_level)
    
    return compressed_data

def lzma_decompress(compressed_data: bytes) -> bytes:
    """
    Decompress LZMA compressed data.

    Args:
        compressed_data (bytes): The LZMA compressed data.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        lzma.LZMAError: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Decompress data
    try:
        decompressed_data = lzma.decompress(compressed_data)
    except lzma.LZMAError as e:
        raise lzma.LZMAError(f"Decompression failed: {e}")
    
    return decompressed_data