"""
Problem:
    - Given an array of integers, find the pair of adjacent
    elements that has the largest product and return that product.
Input:
    - array: An array of integers containing at least two elements.
Output:
    - The largest product of adjacent elements.
"""


from typing import List


def adjacentElementsProduct(inputArray: List[int]) -> int:
    max = inputArray[0] * inputArray[1]
    
    for i in range(len(inputArray)):
        try:
            if inputArray[i] * inputArray[i+1] > max:
                max = inputArray[i] * inputArray[i+1]
        except IndexError:        
            return max

    
print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))