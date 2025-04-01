import typing

def find_kth_smallest(arr: typing.List[int], k: int) -> int:
    """
    Find the kth smallest element in an array using the QuickSelect algorithm.
    
    Args:
        arr (List[int]): Input array of integers
        k (int): The k-th smallest element to find (1-based index)
    
    Returns:
        int: The kth smallest element in the array
    
    Raises:
        ValueError: If k is invalid (less than 1 or greater than array length)
        TypeError: If input is not a list or contains non-integer elements
    
    Time Complexity: O(n) average case, O(n^2) worst case
    Space Complexity: O(1)
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}, got {k}")
    
    def partition(left: int, right: int) -> int:
        """
        Partition the array and return the pivot index.
        
        Uses the rightmost element as pivot and places it in its correct position.
        """
        pivot = arr[right]
        i = left - 1
        
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1
    
    def quick_select(left: int, right: int) -> int:
        """
        QuickSelect implementation to find kth smallest element.
        """
        if left == right:
            return arr[left]
        
        pivot_index = partition(left, right)
        
        # Adjust k to 0-based index
        adjusted_k = k - 1
        
        if adjusted_k == pivot_index:
            return arr[pivot_index]
        elif adjusted_k < pivot_index:
            return quick_select(left, pivot_index - 1)
        else:
            return quick_select(pivot_index + 1, right)
    
    return quick_select(0, len(arr) - 1)