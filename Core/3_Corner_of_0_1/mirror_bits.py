"""
Problem:
    - Reverse the order of the bits in a given integer.

Example:
    - For a = 97, the output should be
      mirrorBits(a) = 67.

    97 equals to 1100001 in binary, which is 1000011 after
    mirroring, and that is 67 in base 10.

Input:
    - a: int

Output:
    - int
"""


def mirrorBits(a: int) -> int:
    x = bin(a)[2:][::-1]
    return sum([int(x[i]) * 2**(len(x)-(i+1)) for i in range(len(x)-1, -1, -1)])


print(mirrorBits(97))