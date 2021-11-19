"""
Problem:
    - Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

    - For
        picture = ["abc", "ded"]
    the output should be

        solution(picture) = ["*****", "*abc*", "*ded*", "*****"]
"""


def solution(picture):
    new_pic = ['*' + i + '*' for i in picture]
    x = '*' * len(new_pic[0])
    return [x] + new_pic + [x]


print(solution(["abc", "ded"]))