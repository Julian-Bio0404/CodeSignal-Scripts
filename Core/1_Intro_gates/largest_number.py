"""
Problem:
    - Given an integer n, return the largest number
    that contains exactly n digits.
Input:
    - int
Output:
    - The largest integer of length n.
"""


def largestNumber(n: int) -> int:
    max = '9'
    return int(max * n)

print(largestNumber(3))