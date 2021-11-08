"""
Problem:
    - Given a divisor and a bound, find the largest integer N such that:
    N is divisible by divisor.
    N is less than or equal to bound.
    N is greater than 0.
    It is guaranteed that such a number exists.

Input:
    - divisor: int
    - bound: int

Output:
    - The largest integer not greater than bound that is divisible by divisor.
"""


def maxMultiple(divisor: int, bound: int) -> int:
    result = bound - (bound % divisor)
    return result

print(maxMultiple(3, 9))