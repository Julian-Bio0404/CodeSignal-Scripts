"""
Problem:
    - Given the string, check if it is a palindrome.
Input:
    - inputString: A non-empty string consisting of lowercase characters.
Output:
    - true if inputString is a palindrome, false otherwise.
"""


def checkPalindrome(inputString: str) -> bool:
    invertida = inputString[::-1]
    invertida = invertida.replace(' ', '').lower()
    inputString = inputString.replace(' ', '').lower()
    
    if inputString == invertida:
        return True
    return False


print(checkPalindrome('Dabale arroz a la zorra el abad'))