#Given a sequence of integers as an array, determine whether it is possible to obtain a strictly 
#increasing sequence by removing no more than one element from the array.

def solution(sequence):
    cont = 0
    aux_lst = sequence[:]
    
    if sequence[0] > sequence[1]:
        sequence.pop(0)
    
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence [i + 1]:
            
            if sequence[i - 1]  == sequence[i + 1]:
                aux_lst.pop(i + 1)
                cont += 1
                break
            
            if sequence[i - 1] > sequence [i + 1]:
                aux_lst.pop(i + 1)
                cont += 1
                break
            
            aux_lst.pop(i)
            cont += 1
            break
    
    
    for i in range(len(aux_lst) - 1):
        if aux_lst[i] >= aux_lst[i + 1]:
            cont += 1
    
    if cont >= 2:
        return False
    else:
        return True