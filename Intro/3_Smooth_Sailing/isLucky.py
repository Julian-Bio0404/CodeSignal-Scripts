"""
Problem:
    - Ticket numbers usually consist of an even number of digits.
    A ticket number is considered lucky if the sum of the first
    half of the digits is equal to the sum of the second half.

    Given a ticket number n, determine if it's lucky or not.
"""


def isLucky(n: int) -> bool:
    r1 = r2 = 0
    for i in str(n)[:len(str(n))//2]:
        r1 += int(i)
    
    for i in str(n)[len(str(n))//2:]:
        r2 += int(i)
    return r1 == r2


print(isLucky(1230))