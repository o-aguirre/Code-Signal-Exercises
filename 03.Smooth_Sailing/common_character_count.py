#Given two strings, find the number of common characters between them.

def solution(s1, s2):
    s2 = list(s2)
    cont = 0
    
    for i in s1:
        if i in s2:
            cont += 1
            s2.remove(i)
    return cont