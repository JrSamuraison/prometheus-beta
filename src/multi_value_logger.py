import logging
from typing import Any, Optional

def log_multiple_values(*values: Any, level: str = 'info', logger: Optional[logging.Logger] = None) -> None:
    """
    Log multiple values in a single statement with flexible logging options.

    Args:
        *values: Variable number of values to be logged.
        level: Logging level (default: 'info'). 
               Supported levels: 'debug', 'info', 'warning', 'error', 'critical'.
        logger: Optional custom logger. If not provided, uses the root logger.

    Raises:
        ValueError: If an invalid logging level is provided.

    Example:
        >>> log_multiple_values(1, "hello", [1, 2, 3])
        # Logs: "1 hello [1, 2, 3]" at INFO level
        
        >>> log_multiple_values("Error", 42, level='error')
        # Logs: "Error 42" at ERROR level
    """
    # Exit early if no values are provided
    if not values:
        return

    # Select the logger
    target_logger = logger or logging.getLogger()

    # Normalize the logging level
    level = level.lower()
    log_levels = {
        'debug': target_logger.debug,
        'info': target_logger.info,
        'warning': target_logger.warning,
        'error': target_logger.error,
        'critical': target_logger.critical
    }

    # Validate logging level
    if level not in log_levels:
        raise ValueError(f"Invalid logging level: {level}. "
                         f"Supported levels are: {', '.join(log_levels.keys())}")

    # Convert values to strings and join them
    log_message = ' '.join(str(value) for value in values)

    # Log the message at the specified level
    log_levels[level](log_message)