import sys

def log_error(message, error_type=None):
    """
    Log an error message to the console.

    Args:
        message (str): The error message to log.
        error_type (str, optional): The type of error. Defaults to None.

    Raises:
        TypeError: If message is not a string.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Error message must be a string")
    
    # Construct error message
    error_output = f"ERROR: {message}"
    if error_type:
        error_output = f"{error_type.upper()} {error_output}"
    
    # Log to standard error stream
    print(error_output, file=sys.stderr)