"""
Problem:
    - Given integers a and b, determine whether the following
    pseudocode results in an infinite loop:

        while a is not equal to b do
        increase a by 1
        decrease b by 1

    Assume that the program is executed on a virtual machine
    which can store arbitrary long numbers and execute forever.

Input:
    - a: int
    - b: int

Output:
    - true if the pseudocode will never stop, false otherwise.
"""


def isInfiniteProcess(a: int, b: int) -> bool:
    if b - a >= 0:
        return (b - a) % 2 != 0
    return True


print(isInfiniteProcess(2, 6))
print(isInfiniteProcess(10, 10))
print(isInfiniteProcess(2, 3))