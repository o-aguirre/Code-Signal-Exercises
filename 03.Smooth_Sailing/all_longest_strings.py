#Given an array of strings, return another array containing all of its longest strings.

def solution(inputArray):
    longer = ['']
    for i in inputArray:
        if len(i) > len(longer[0]):
            longer.clear()
            longer.append(i)
        elif len(i) == len(longer[0]):
            longer.append(i)
    return longer