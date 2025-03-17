def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature converted to Celsius, rounded to 2 decimal places.

    Raises:
        TypeError: If input is not a number (int or float).
    """
    # Check if input is a number
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    
    # Conversion formula: (°F - 32) × 5/9
    celsius = (fahrenheit - 32) * 5/9
    
    # Round to 2 decimal places for precision
    return round(celsius, 2)