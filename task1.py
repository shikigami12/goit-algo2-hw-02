"""
Task 1: Finding Maximum and Minimum Elements using Divide and Conquer

This module implements a function to find both the maximum and minimum
elements in an array using the divide and conquer approach.

Time Complexity: O(n)
Space Complexity: O(log n) due to recursion stack
"""

from typing import List, Tuple


def find_min_max(arr: List[int | float]) -> Tuple[int | float, int | float]:
    """
    Find the minimum and maximum elements in an array using divide and conquer.

    Args:
        arr: List of numbers (integers or floats)

    Returns:
        Tuple containing (minimum, maximum)

    Raises:
        ValueError: If array is empty

    Examples:
        >>> find_min_max([3, 1, 4, 1, 5, 9, 2, 6])
        (1, 9)
        >>> find_min_max([42])
        (42, 42)
        >>> find_min_max([5, 2])
        (2, 5)
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    return _find_min_max_recursive(arr, 0, len(arr) - 1)


def _find_min_max_recursive(arr: List[int | float], left: int, right: int) -> Tuple[int | float, int | float]:
    """
    Recursive helper function to find min and max using divide and conquer.

    Args:
        arr: The array to search
        left: Left boundary index
        right: Right boundary index

    Returns:
        Tuple containing (minimum, maximum) in the range [left, right]
    """
    if left == right:
        return arr[left], arr[left]

    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    mid = (left + right) // 2

    left_min, left_max = _find_min_max_recursive(arr, left, mid)
    right_min, right_max = _find_min_max_recursive(arr, mid + 1, right)

    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)

    return overall_min, overall_max


def test_find_min_max():
    """Test function with various test cases."""
    print("Testing find_min_max function:\n")

    test1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    min_val, max_val = find_min_max(test1)
    print(f"Test 1: {test1}")
    print(f"Result: min = {min_val}, max = {max_val}\n")

    test2 = [42]
    min_val, max_val = find_min_max(test2)
    print(f"Test 2: {test2}")
    print(f"Result: min = {min_val}, max = {max_val}\n")

    test3 = [10, 5]
    min_val, max_val = find_min_max(test3)
    print(f"Test 3: {test3}")
    print(f"Result: min = {min_val}, max = {max_val}\n")

    test4 = [-5, -1, -10, -3, -7]
    min_val, max_val = find_min_max(test4)
    print(f"Test 4: {test4}")
    print(f"Result: min = {min_val}, max = {max_val}\n")

    test5 = [-10, 20, -5, 30, 0, 15, -20, 25]
    min_val, max_val = find_min_max(test5)
    print(f"Test 5: {test5}")
    print(f"Result: min = {min_val}, max = {max_val}\n")

    test6 = [7, 7, 7, 7, 7]
    min_val, max_val = find_min_max(test6)
    print(f"Test 6: {test6}")
    print(f"Result: min = {min_val}, max = {max_val}\n")

    test7 = [3.14, 2.71, 1.41, 1.73, 2.23]
    min_val, max_val = find_min_max(test7)
    print(f"Test 7: {test7}")
    print(f"Result: min = {min_val}, max = {max_val}\n")

    test8 = list(range(100, 0, -1))
    min_val, max_val = find_min_max(test8)
    print(f"Test 8: Array from 100 down to 1")
    print(f"Result: min = {min_val}, max = {max_val}\n")


if __name__ == "__main__":
    test_find_min_max()
