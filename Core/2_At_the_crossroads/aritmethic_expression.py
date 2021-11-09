"""
Problem:
    - Consider an arithmetic expression of the form a#b=c.
    Check whether it is possible to replace # with one of
    the four signs: +, -, * or / to obtain a correct expression.

Input:
    - a: int
    - b: int
    - c: int

Output:
    - true if the desired replacement is possible, false otherwise.
"""


def arithmeticExpression(a: int, b: int, c: int) -> bool:
    return a / b == c or a + b == c or a - b == c or a * b == c


print(arithmeticExpression(2, 3, 5))