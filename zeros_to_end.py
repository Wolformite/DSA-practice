# Problem: Move Zeros to End
# Time Complexity: O(n)
# Space Complexity: O(1)

def move_zeros(arr):
    n = len(arr)
    pos = 0  # position for next non-zero

    for i in range(n):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1

    return arr
