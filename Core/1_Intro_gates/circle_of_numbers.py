"""
problem:
    - Consider integer numbers from 0 to n - 1 written down along
    the circle in such a way that the distance between any two
    neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

    Given n and firstNumber, find the number which is written in the
    radially opposite position to firstNumber.

Example:
    - For n = 10 and firstNumber = 2, the output should be
      circleOfNumbers(n, firstNumber) = 7.

Input:
    - n: A positive even integer.
    - firstNumber: A integer 0 ≤ firstNumber ≤ n - 1.

Output:
    - int
"""

def circleOfNumbers(n: int, firstNumber: int) -> int:
    center = n / 2
    if firstNumber < center:
        return center + firstNumber
    return firstNumber - center