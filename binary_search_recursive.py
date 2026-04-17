"""
Binary Search Implementation (Recursive)
Condition: The array MUST be sorted.
Time Complexity: Best Case: O(1) , Average/Worst Case: O(log n)
Space Complexity: O(log n) (due to recursion stack)
"""

def binary_search_recursive(arr, left, right, target):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, right, target)
    else:
        return binary_search_recursive(arr, left, mid - 1, target)

