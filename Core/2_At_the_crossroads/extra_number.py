"""
Problem:
    - You're given three integers, a, b and c. It is guaranteed
    that two of these integers are equal to each other. What is
    the value of the third integer?

Input:
    - a: int
    - b: int
    - c: int

Output:
    - int
"""


def extraNumber(a: int, b: int, c: int) -> int:
    if a not in [b, c]:
        return a
    if b not in [a, c]:
        return b
    return c


print(extraNumber(2, 7, 2))