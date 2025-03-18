import time
from functools import wraps
from typing import Callable, Any


def measure_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures and prints the execution time of a function.

    Args:
        func (Callable): The function whose execution time is to be measured.

    Returns:
        Callable: A wrapped function that prints its execution time.

    Example:
        @measure_execution_time
        def example_function():
            # Function implementation
            pass
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrap the original function to measure its execution time.

        Args:
            *args: Positional arguments to pass to the original function.
            **kwargs: Keyword arguments to pass to the original function.

        Returns:
            The result of the original function.
        """
        # Record start time
        start_time = time.perf_counter()

        try:
            # Execute the function
            result = func(*args, **kwargs)
        except Exception as e:
            # If an exception occurs, re-raise it after printing execution time
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
            raise

        # Record end time and calculate execution time
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # Print execution time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")

        return result

    return wrapper