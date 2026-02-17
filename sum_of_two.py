# Problem: Adding two nums to get to target
# Time Complexity: O(n)
# Space Complexity: O(n)

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return -1
