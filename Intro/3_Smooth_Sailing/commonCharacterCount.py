"""
Problem:
    - Given two strings, find the number of common characters between them.

Example:
    - For s1 = "aabcc" and s2 = "adcaa", the output should be
      commonCharacterCount(s1, s2) = 3.

    Strings have 3 common characters - 2 "a"s and 1 "c".
"""

def commonCharacterCount(s1: str, s2: str):
    x = 0
    s2 = list(s2)

    for i in s1:
        if i in s2:
            x += 1
        for j in range(len(s2)):
            if s2[j] == i:
               s2.pop(j)
               break
    return x


print(commonCharacterCount('aabcc', 'adcaa'))