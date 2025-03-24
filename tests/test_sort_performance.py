import pytest
import random
from src.sort_performance import compare_sorting_algorithms, bubble_sort, quick_sort

def test_compare_sorting_algorithms_basic():
    """Test basic functionality of performance comparison"""
    # Generate a random list of integers
    test_arr = [random.randint(1, 1000) for _ in range(100)]
    
    # Compare bubble sort and quick sort
    result = compare_sorting_algorithms(
        test_arr, 
        bubble_sort, 
        quick_sort, 
        'Bubble Sort', 
        'Quick Sort'
    )
    
    # Verify result structure
    assert 'results' in result
    assert 'comparison' in result
    
    # Check algorithm names
    assert 'Bubble Sort' in result['results']
    assert 'Quick Sort' in result['results']
    
    # Verify performance metrics
    assert 'runtime_ms' in result['results']['Bubble Sort']
    assert 'runtime_ms' in result['results']['Quick Sort']
    
    # Verify sorted arrays
    assert result['results']['Bubble Sort']['sorted_array'] == sorted(test_arr)
    assert result['results']['Quick Sort']['sorted_array'] == sorted(test_arr)
    
    # Verify comparison keys
    assert 'faster_algorithm' in result['comparison']
    assert 'performance_difference_ms' in result['comparison']

def test_compare_sorting_algorithms_empty_list():
    """Test performance comparison with an empty list"""
    test_arr = []
    
    result = compare_sorting_algorithms(
        test_arr, 
        bubble_sort, 
        quick_sort, 
        'Bubble Sort', 
        'Quick Sort'
    )
    
    # Verify empty list is sorted correctly
    assert result['results']['Bubble Sort']['sorted_array'] == []
    assert result['results']['Quick Sort']['sorted_array'] == []

def test_compare_sorting_algorithms_already_sorted():
    """Test performance comparison with an already sorted list"""
    test_arr = list(range(100))
    
    result = compare_sorting_algorithms(
        test_arr, 
        bubble_sort, 
        quick_sort, 
        'Bubble Sort', 
        'Quick Sort'
    )
    
    # Verify sorted list remains sorted
    assert result['results']['Bubble Sort']['sorted_array'] == test_arr
    assert result['results']['Quick Sort']['sorted_array'] == test_arr

def test_compare_sorting_algorithms_negative_numbers():
    """Test performance comparison with negative numbers"""
    test_arr = [random.randint(-1000, 1000) for _ in range(100)]
    
    result = compare_sorting_algorithms(
        test_arr, 
        bubble_sort, 
        quick_sort, 
        'Bubble Sort', 
        'Quick Sort'
    )
    
    # Verify sorted correctly
    assert result['results']['Bubble Sort']['sorted_array'] == sorted(test_arr)
    assert result['results']['Quick Sort']['sorted_array'] == sorted(test_arr)

def test_invalid_sorting_algorithm():
    """Test with a sorting algorithm that doesn't actually sort"""
    def bad_sort(arr):
        return arr  # Does not actually sort
    
    with pytest.raises(ValueError, match="Sorting algorithms did not produce correct results"):
        compare_sorting_algorithms(
            [3, 1, 2], 
            bad_sort, 
            quick_sort, 
            'Bad Sort', 
            'Quick Sort'
        )