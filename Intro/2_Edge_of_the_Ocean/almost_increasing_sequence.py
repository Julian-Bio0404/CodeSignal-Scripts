"""
Problem:
    - Given a sequence of integers as an array, determine
    whether it is possible to obtain a strictly increasing
    sequence by removing no more than one element from the
    array.

    - Note: sequence a0, a1, ..., an is considered to be
    a strictly increasing if a0 < a1 < ... < an. Sequence
    containing only one element is also considered to be
    strictly increasing.

Example:
    - For sequence = [1, 3, 2, 1], the output should be
      almostIncreasingSequence(sequence) = false.
    There is no one element in this array that can be
    removed in order to get a strictly increasing sequence.
    - For sequence = [1, 3, 2], the output should be
      almostIncreasingSequence(sequence) = true.
    You can remove 3 from the array to get the strictly
    increasing sequence [1, 2]. Alternately, you can remove
    2 to get the strictly increasing sequence [1, 3].

Input:
    - sequence: an array integer sequence

Output:
    - Return true if it is possible to remove one element
    from the array in order to get a strictly increasing
    sequence, otherwise return false.
"""


def almostIncreasingSequence(sequence: list[int]) -> bool:
    removed = False
    latest = previous = min(sequence) - 1
    for i in sequence:
        if i <= latest:
            if removed:
                return False
            removed = True
            if i <= previous:
                previous = latest
            elif i >= previous:
                previous = latest = i
        else:
            previous, latest = latest, i
    return True

print(almostIncreasingSequence([1, 2, 1, 2]))