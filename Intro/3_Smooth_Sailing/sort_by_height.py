""""
Problem:
    - Some people are standing in a row in a park. There are trees between them
    which cannot be moved. Your task is to rearrange the people by their heights
    in a non-descending order without moving the trees. People can be very tall!

Example:
    - For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
      solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190]
"""


def solution(a: list[int]) -> list[int]:
    result = []
    persons = sorted([i for i in a if i != -1])
    y = z = 0

    for i in range(y, len(a)):
        if a[i] == -1:
            y += 1
            result.append(a[i])
        else:
            for j in range(z, len(persons)):
                if a[y] != -1:
                    result.append(persons[j])
                    z += 1
                    y += 1
                else:
                    break
    return result


print(solution([-1, 150, 190, 170, -1, -1, 160, 180]))