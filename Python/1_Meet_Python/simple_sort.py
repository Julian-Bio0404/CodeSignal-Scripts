"""
Problem:
    - To understand how efficient the built-in Python sorting function is,
    you decided to implement your own simple sorting algorithm and compare
    its speed to the speed of the Python sorting. Write a function that,
    given an array of integers arr, sorts its elements in ascending order.

    Hint: with Python it's possible to swap several elements in a single
    line
"""


def solution(arr: list[int]) -> int:
    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j += 1
    return arr


print(solution([2, 4, 1, 5]))