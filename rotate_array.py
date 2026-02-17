# Problem: Rotate Array 
# Time Complexity: O(n)
# Space Complexity: O(1)

def rotate_array(arr, k):
    n = len(arr)
    k %= n

    arr[:] = arr[-k:] + arr[:-k]
    return arr
