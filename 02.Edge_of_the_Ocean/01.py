#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

def solution(inputArray):
    mayor = inputArray[0] * inputArray[1]
    for i in range(0, len(inputArray) - 1):
        mult = inputArray[i] * inputArray[i + 1]
        if mult > mayor: mayor = mult
    return mayor