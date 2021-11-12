"""
Problem:
    - In order to stop the Mad Coder evil genius you need to decipher
    the encrypted message he sent to his minions. The message contains
    several numbers that, when typed into a supercomputer, will launch
    a missile into the sky blocking out the sun, and making all the
    people on Earth grumpy and sad.

    You figured out that some numbers have a modified single digit in
    their binary representation. More specifically, in the given number
    n the kth bit from the right was initially set to 0, but its current
    value might be different. It's now up to you to write a function
    that will change the kth bit of n back to 0.

Example:
    - For n = 37 and k = 3, the output should be
      killKthBit(n, k) = 33.

    3710 = 1001012 ~> 1000012 = 3310.

    - For n = 37 and k = 4, the output should be
      killKthBit(n, k) = 37.

    The 4th bit is 0 already (looks like the Mad Coder forgot to encrypt
    this number), so the answer is still 37.

Input:
    - n: int
    - k: int

Output:
    - int
"""


def decimal_binary(n: int) -> str:
    binary = ''
    while n != 1:
        binary += str(n % 2)
        n //= 2
    return '1' + binary[::-1]


def binary_decimal(n: int) -> int:
    return sum([2 ** i * int(n[::-1][i]) for i in range(len(n[::-1]))])


if __name__ == '__main__':

    def killKthBit(n: int, k: int) -> int:
        binary = decimal_binary(n)
        if binary[k] == 0:
            return n
        binary = list(binary)
        binary[k] = 0
        return binary_decimal(binary)

    print(killKthBit(37, 3))