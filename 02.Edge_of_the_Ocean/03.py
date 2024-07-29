#Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. 
# Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. 
# He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

def solution(statues):
    menor = statues[0]
    mayor = statues[0]
    faltan = 0
    for i in statues:
        if i < menor: menor = i
        if i > mayor: mayor = i
    for i in range(menor, mayor):
        if i not in statues:
            faltan += 1
    return faltan

