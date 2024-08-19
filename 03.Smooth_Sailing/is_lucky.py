def solution(n):
    n = list(str(n))
    half = int(len(n)/2)
    f_half = n[:half]
    s_half = n[half:len(n)]
    
    sum_1 = 0
    sum_2 = 0
    for i in f_half:
        sum_1 += int(i)
    for i in s_half:
        sum_2 += int(i)
    
    if sum_1 == sum_2:
        return True
    else:
        return False
    