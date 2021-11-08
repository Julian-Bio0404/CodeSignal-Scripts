"""
Problem:
    - You found two items in a treasure chest! The first item weighs
    weight1 and is worth value1, and the second item weighs weight2
    and is worth value2. What is the total maximum value of the items
    you can take with you, assuming that your max weight capacity is
    maxW and you can't come back for the items later?
    Note that there are only two items and you can't bring more than
    one item of each type, i.e. you can't take two first items or two
    second items.

Input:
    - value1: int
    - weight: int
    - value2: int
    - weight2: int
    - maxW: int

Output:
    - int
"""

def knapsackLight(
    value1: int, weight1: int, value2: int, weight2: int, maxW: int) -> int:
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        if weight1 <= maxW and weight2 <= maxW:
            if value1 > value2:
                return value1
            return value2
        elif weight1 <= maxW:
            return value1
        elif weight2 <= maxW:
            return value2
        return 0