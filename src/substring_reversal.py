def reverse_substring(s: str, start: int, end: int) -> str:
    """
    Reverse a substring within a given string.

    Args:
        s (str): The input string.
        start (int): The starting index of the substring to reverse (inclusive).
        end (int): The ending index of the substring to reverse (exclusive).

    Returns:
        str: A new string with the specified substring reversed.

    Raises:
        ValueError: If start or end indices are out of bounds.
        ValueError: If start index is greater than end index.
    """
    # Validate input indices
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if not (0 <= start <= len(s)):
        raise ValueError(f"Start index {start} is out of bounds for string of length {len(s)}")
    
    if not (0 <= end <= len(s)):
        raise ValueError(f"End index {end} is out of bounds for string of length {len(s)}")
    
    if start > end:
        raise ValueError(f"Start index {start} cannot be greater than end index {end}")
    
    # Reverse the specified substring
    return s[:start] + s[start:end][::-1] + s[end:]