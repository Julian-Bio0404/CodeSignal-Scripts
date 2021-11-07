"""
Problem:
    - Given a year, return the century it is in.
    The first century spans from the year 1 up to and
    including the year 100, the second - from the year
    101 up to and including the year 200, etc.
Input:
    - year: A positive integer, designating the year.
Output:
    - The number of the century the year is in.
"""


def centuryFromYear(year: int) -> int:
    if year < 100:
        century = 1
    elif year < 1000:
        if str(year)[1:3] == '00':
            century = int(str(year)[0:1])
        else:
            century = int(str(year)[0:1]) + 1
    else:
        if str(year)[2:4] == '00':
            century = int(str(year)[0:2])
        else:
            century = int(str(year)[0:2]) + 1
    return century


print(centuryFromYear(99))