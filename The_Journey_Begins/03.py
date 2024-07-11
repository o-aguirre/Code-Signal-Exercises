#Given the string, check if it is a palindrome.

def solution(inputString):
    p_word = ''
    for i in range(len(inputString), 0, -1):
        p_word += inputString[i - 1]
    if inputString == p_word:
        return True
    else:
        return False