# Problem: Fibonacci with Memoization (Top-Down DP)
# Approach:
# Store already computed Fibonacci values in a dictionary (memo)
# to avoid repeated calculations.
#
# Time Complexity: O(n)
# Each Fibonacci value from 0 → n is computed only once.
#
# Space Complexity: O(n)
# O(n) for recursion call stack + O(n) for memo dictionary.

def fibonacci_memo(n, memo={}):
    # If value already computed → return from memory
    if n in memo:
        return memo[n]
    # Base case (stopping condition)
    if n <= 1:
        return n
    # Store computed result
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]
