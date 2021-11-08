"""
Problem:
    - n children have got m pieces of candy. They want to eat as
    much candy as they can, but each child must eat exactly the
    same amount of candy as any other child. Determine how many
    pieces of candy will be eaten by all the children together.
    Individual pieces of candy cannot be split.

Input:
    - n: The number of children.
    - m: The number of pieces of candy.

Output:
    - The total number of pieces of candy.
"""

from math import floor


def candies(n: int, m: int) -> int:
    return floor(m / n) * n


print(candies(3, 10))