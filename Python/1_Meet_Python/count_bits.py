"""
Problem:
    - Implement a function that, given an integer n, uses a specific
    method on it and returns the number of bits in its binary
    representation.
"""


def solution(n):
    return n.bit_length()


print(solution(50))