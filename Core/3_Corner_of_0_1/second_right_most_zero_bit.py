"""
Problem:
    - Presented with the integer n, find the 0-based position
    of the second rightmost zero bit in its binary representation
    (it is guaranteed that such a bit exists), counting from right
    to left.

    Return the value of 2nd position of the found bit.

Example:
    - For n = 37, the output should be
      secondRightmostZeroBit(n) = 8.

    3710 = 1001012. The second rightmost zero bit is at position 3
    (0-based) from the right in the binary representation of n.
    Thus, the answer is 23 = 8.
"""


def secondRightmostZeroBit(n: int) -> int:
    return 2 ** [i for i in range(0, len(bin(n)[2::])) if bin(n)[:1:-1][i] == '0'][1]


print(secondRightmostZeroBit(37))