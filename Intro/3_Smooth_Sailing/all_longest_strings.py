"""
Problem:
    - Given an array of strings, return another
    array containing all of its longest strings.
"""


def allLongestStrings(inputArray: list[str]) -> list[str]:
    longest = len(inputArray[0])
    
    for i in inputArray:
        if len(i) > longest:
            longest = len(i)
    return [i for i in inputArray if len(i) == longest]