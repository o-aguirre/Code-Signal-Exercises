#Given matrix, a rectangular matrix of integers, where each value represents the cost of the room,
#your task is to return the total sum of all rooms that are suitable for the CodeBots
#(ie: add up all the values that don't appear below a 0).

def solution(matrix):
    sum = 0
    column_pass = []
    for row in matrix:
        for e in range(len(row)):
            if row[e] == 0:
                if e not in column_pass:
                    column_pass.append(e)
            
            else:
                if e not in column_pass:
                    sum += row[e]           
                    
    return sum