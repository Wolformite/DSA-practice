"""
Binary Search Implementation (Iterative)
Condition: The array MUST be sorted.
Time Complexity: Best Case: O(1) , Average/Worst Case: O(log n)
Space Complexity: O(1) 
"""

def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # avoids overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

