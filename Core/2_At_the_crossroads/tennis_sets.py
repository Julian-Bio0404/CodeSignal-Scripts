"""
Problem:
    - In tennis, the winner of a set is based on how many games each player wins.
    The first player to win 6 games is declared the winner unless their opponent
    had already won 5 games, in which case the set continues until one of the
    players has won 7 games.
    Given two integers score1 and score2, your task is to determine if it is possible
    for a tennis set to be finished with a final score of score1 : score2.

Input:
    - score1: Number of games won by the 1st player, non-negative integer.
    - socore2: Number of games won by the 2nd player, non-negative integer.

Output:
    - true if score1 : score2 represents a possible score for an ended set,
    false otherwise.
"""


def tennisSet(score1, score2):
    minscore, maxscore = min(score1, score2), max(score1, score2)
    return (maxscore == 6 and minscore < 5) or (maxscore == 7 and minscore in (5,6))


print(tennisSet(3, 6))
print(tennisSet(7, 2))