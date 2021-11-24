"""
Problem:
    - Implement the missing code, denoted by ellipses.
    You may not modify the pre-existing code.

    Given a word, check whether it is a palindrome or not.
    A string is considered to be a palindrome if it reads
    the same in both directions.
"""


def solution(word: str) -> bool:
    return word == word[::-1]


print(solution("aibohphobia"))