import calendar
from datetime import date

def count_weekends_in_month(year: int, month: int) -> int:
    """
    Count the number of weekend days (Saturdays and Sundays) in a given month.

    Args:
        year (int): The year to check (e.g., 2023)
        month (int): The month to check (1-12)

    Returns:
        int: Number of weekend days in the specified month

    Raises:
        ValueError: If the month is not between 1 and 12
    """
    # Validate month input
    if not 1 <= month <= 12:
        raise ValueError("Month must be between 1 and 12")

    # Get the number of days in the month
    _, num_days = calendar.monthrange(year, month)

    # Count weekend days
    weekend_count = 0
    for day in range(1, num_days + 1):
        # Create a date object for each day in the month
        current_date = date(year, month, day)
        
        # Check if the day is a Saturday (5) or Sunday (6)
        if current_date.weekday() in [5, 6]:
            weekend_count += 1

    return weekend_count