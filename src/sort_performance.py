import time
import random
from typing import List, Callable, Tuple

def compare_sorting_algorithms(
    arr: List[int], 
    algo1: Callable[[List[int]], List[int]], 
    algo2: Callable[[List[int]], List[int]], 
    algo1_name: str = 'Algorithm 1', 
    algo2_name: str = 'Algorithm 2'
) -> dict:
    """
    Compare the performance of two sorting algorithms.
    
    Args:
        arr (List[int]): Input list to be sorted
        algo1 (Callable): First sorting algorithm function
        algo2 (Callable): Second sorting algorithm function
        algo1_name (str, optional): Name of the first algorithm. Defaults to 'Algorithm 1'.
        algo2_name (str, optional): Name of the second algorithm. Defaults to 'Algorithm 2'.
    
    Returns:
        dict: Performance comparison results including runtime and memory usage
    """
    # Create deep copies to ensure fair comparison
    arr1 = arr.copy()
    arr2 = arr.copy()
    
    # Measure performance of first algorithm
    start_time1 = time.perf_counter()
    sorted_arr1 = algo1(arr1)
    end_time1 = time.perf_counter()
    runtime1 = (end_time1 - start_time1) * 1000  # Convert to milliseconds
    
    # Measure performance of second algorithm
    start_time2 = time.perf_counter()
    sorted_arr2 = algo2(arr2)
    end_time2 = time.perf_counter()
    runtime2 = (end_time2 - start_time2) * 1000  # Convert to milliseconds
    
    # Validate results are correctly sorted
    if sorted_arr1 != sorted(arr) or sorted_arr2 != sorted(arr):
        raise ValueError("Sorting algorithms did not produce correct results")
    
    return {
        'results': {
            algo1_name: {
                'runtime_ms': runtime1,
                'sorted_array': sorted_arr1
            },
            algo2_name: {
                'runtime_ms': runtime2,
                'sorted_array': sorted_arr2
            }
        },
        'comparison': {
            'faster_algorithm': algo1_name if runtime1 < runtime2 else algo2_name,
            'performance_difference_ms': abs(runtime1 - runtime2)
        }
    }

# Example sorting algorithms for testing
def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble sort implementation for demonstration.
    
    Args:
        arr (List[int]): Input list to be sorted
    
    Returns:
        List[int]: Sorted list
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick sort implementation for demonstration.
    
    Args:
        arr (List[int]): Input list to be sorted
    
    Returns:
        List[int]: Sorted list
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)