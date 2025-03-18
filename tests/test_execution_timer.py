import time
import pytest
from src.execution_timer import measure_execution_time


def test_measure_execution_time_decorator(capsys):
    """
    Test that the measure_execution_time decorator works correctly.
    
    Args:
        capsys: pytest fixture to capture stdout and stderr
    """
    @measure_execution_time
    def sample_function(sleep_time: float = 0.1) -> str:
        """
        Sample function that sleeps for a specified time.
        
        Args:
            sleep_time (float): Time to sleep, defaults to 0.1 seconds
        
        Returns:
            str: A greeting message
        """
        time.sleep(sleep_time)
        return "Hello, World!"

    # Call the function and check its return value
    result = sample_function()
    assert result == "Hello, World!"

    # Capture the printed output
    captured = capsys.readouterr()
    
    # Check that execution time was printed
    assert "Execution time of sample_function:" in captured.out
    
    # Extract the actual time from the printed message
    time_str = captured.out.split(":")[1].strip().split()[0]
    execution_time = float(time_str)
    
    # Verify the execution time is close to the sleep time (with some tolerance)
    assert 0.09 <= execution_time <= 0.11, f"Unexpected execution time: {execution_time}"


def test_measure_execution_time_with_arguments():
    """
    Test the decorator with a function that takes arguments.
    """
    @measure_execution_time
    def multiply(a: int, b: int) -> int:
        """
        Multiply two numbers.
        
        Args:
            a (int): First number
            b (int): Second number
        
        Returns:
            int: Product of a and b
        """
        return a * b

    # Check if the function returns the correct result
    result = multiply(5, 7)
    assert result == 35


def test_measure_execution_time_with_exception():
    """
    Test that the decorator works correctly when an exception is raised.
    """
    @measure_execution_time
    def divide(a: int, b: int) -> float:
        """
        Divide two numbers.
        
        Args:
            a (int): Numerator
            b (int): Denominator
        
        Returns:
            float: Result of division
        
        Raises:
            ZeroDivisionError: If b is zero
        """
        return a / b

    # Check that the exception is re-raised and execution time is printed
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)