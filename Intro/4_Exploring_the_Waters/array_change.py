"""
Problem:
    - You are given an array of integers. On each move you are allowed to
    increase exactly one of its element by one. Find the minimal number of
    moves required to obtain a strictly increasing sequence from the input.
"""


def solution(inputArray: list[int]) -> int:
    moves = same = 0
    elm = sorted(inputArray)[0] - 1
    for i in inputArray:
        if i <= elm and same == 0:
            moves += elm - i + 1
            elm += 1
        elif same > 0:
            moves += elm + 1
            if i == elm:
                same = 0
            else:
                same += 1
            elm += 1
        else:
            elm = i
    return moves


print(solution([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]))