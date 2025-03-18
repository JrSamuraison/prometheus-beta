import logging
from typing import Union, List

def log_multiline(
    message: Union[str, List[str]], 
    level: int = logging.INFO, 
    separator_char: str = '-', 
    separator_length: int = 50
) -> None:
    """
    Log a multi-line message with optional separation lines.

    Args:
        message (Union[str, List[str]]): Message(s) to log. 
            Can be a single string or a list of strings.
        level (int, optional): Logging level. Defaults to logging.INFO.
        separator_char (str, optional): Character used for separation lines. 
            Defaults to '-'.
        separator_length (int, optional): Length of separation lines. 
            Defaults to 50.

    Raises:
        ValueError: If separator_char is not a single character or 
            separator_length is less than 1.
    """
    # Validate inputs
    if len(separator_char) != 1:
        raise ValueError("Separator must be a single character")
    
    if separator_length < 1:
        raise ValueError("Separator length must be at least 1")

    # Prepare logger
    logger = logging.getLogger(__name__)

    # Convert single string to list if needed
    if isinstance(message, str):
        message = [message]

    # Create separator line
    separator = separator_char * separator_length

    # Log with separators
    logger.log(level, separator)
    for line in message:
        logger.log(level, line)
    logger.log(level, separator)