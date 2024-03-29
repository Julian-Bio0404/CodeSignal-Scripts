"""
Problem:
    - Let's call a list beautiful if its first element is equal to its
    last element, or if a list is empty. Given a list a, your task is
    to chop off its first and its last element until it becomes beautiful.
    Implement a function that will make the given a beautiful as described,
    and return the resulting list as an answer.

    Hint: one of the features introduced in Python 3 called extended
    unpacking could help here. (https://www.python.org/dev/peps/pep-3132/)
"""


def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        _, *res, _ = res
    return res


print(solution([1, 2, 3]))