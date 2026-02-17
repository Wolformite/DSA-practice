# Problem: Remove Duplicates and return new length of array(Sorted Array)
# Time Complexity: O(n)
# Space Complexity: O(1)

def remove_duplicates(arr):
    if not arr:
        return 0

    pos = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[pos] = arr[i]
            pos += 1

    return pos  # new length
