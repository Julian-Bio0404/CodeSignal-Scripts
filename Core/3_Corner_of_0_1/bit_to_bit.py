"""
Problem:
    - Convert binary to decimal and vice versa

Input:
    - int

Output:
    - int
"""


def decimal(n: str) -> int:
    return sum([int(n[i]) * 2**(len(n)-(i+1)) for i in range(len(n)-1, -1, -1)])


def bin(n: int) -> str:
    mods = []
    if n != 0:
        while n != 0:
            mods.insert(0, str(n % 2))
            n //= 2
        return ''.join(mods)
    return str(0)


print(decimal('000000000101010100011000'))
print(bin(2**30))