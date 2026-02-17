# Problem: Check Palindrome String (two pointers)
# Time Complexity: O(n)
# Space Complexity: O(1)

def palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
