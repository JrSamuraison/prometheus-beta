import gzip
import io

def gzip_compress(data):
    """
    Compress input data using Gzip compression.

    Args:
        data (str or bytes): The input data to compress.

    Returns:
        bytes: Compressed data.

    Raises:
        TypeError: If input is not a string or bytes.
        ValueError: If input is empty.
    """
    # Validate input
    if data is None:
        raise ValueError("Input cannot be None")
    
    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes")
    
    # Check for empty input
    if len(data) == 0:
        raise ValueError("Input cannot be empty")
    
    # Perform Gzip compression
    try:
        with io.BytesIO() as bio:
            with gzip.GzipFile(fileobj=bio, mode='wb') as gzipfile:
                gzipfile.write(data)
            return bio.getvalue()
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def gzip_decompress(compressed_data):
    """
    Decompress Gzip compressed data.

    Args:
        compressed_data (bytes): The Gzip compressed data to decompress.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
        RuntimeError: If decompression fails.
    """
    # Validate input
    if compressed_data is None:
        raise ValueError("Input cannot be None")
    
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Check for empty input
    if len(compressed_data) == 0:
        raise ValueError("Input cannot be empty")
    
    # Perform Gzip decompression
    try:
        with io.BytesIO(compressed_data) as bio:
            with gzip.GzipFile(fileobj=bio, mode='rb') as gzipfile:
                return gzipfile.read()
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")