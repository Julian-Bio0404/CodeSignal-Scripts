"""
Problem:
    - You are given two numbers a and b where 0 ≤ a ≤ b.
    Imagine you construct an array of all the integers
    from a to b inclusive. You need to count the number
    of 1s in the binary representations of all the numbers
    in the array.

Example:
    - For a = 2 and b = 7, the output should be
      rangeBitCount(a, b) = 11.

    Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7].
    Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111],
    which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.

Input:
    - a: int
    - b: int

Output:
    - int
"""


def rangeBitCount(a: int, b: int) -> int:
    binaries = [bin(i)[2:] for i in [j for j in range(a, b+1)]]
    total = 0
    for i in binaries:
        for j in i:
            total += int(j)
    return total


print(rangeBitCount(2, 7))