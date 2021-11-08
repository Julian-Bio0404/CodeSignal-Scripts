"""
Problem:
    - You are given a two-digit integer n. Return the sum of its digits.
Input: 
    - int: A positive two-digit integer.
Output:
    - The sum of the first and second digits of the input number.
"""

def addTwoDigits(n: int) -> int:
    n1, n2 = int(str(n)[:1]), int(str(n)[1:])
    return n1 + n2

print(addTwoDigits(29))