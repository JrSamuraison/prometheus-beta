import json

def is_valid_json(json_string):
    """
    Check if the given string represents a valid JSON.

    Args:
        json_string (str): The string to validate as JSON.

    Returns:
        bool: True if the string is valid JSON, False otherwise.
    """
    try:
        # Attempt to parse the string
        json.loads(json_string)
        return True
    except (json.JSONDecodeError, TypeError):
        # Return False if parsing fails or input is not a string
        return False