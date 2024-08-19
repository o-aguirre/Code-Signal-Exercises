def solution(a):
    aux_list = []
    for i in a:
        if i != -1:
            aux_list.append(i)
    aux_list.sort()

    for i in range(len(a)):
        if a[i] != -1:
            a[i] = aux_list[0]
            aux_list.pop(0)

    return a
