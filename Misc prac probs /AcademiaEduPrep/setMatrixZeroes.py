"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

    Input: 
    [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
    Output: 
    [
    [1,0,1],
    [0,0,0],
    [1,0,1]
    ]

Example 2:

    Input: 
    [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]
    Output: 
    [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
    ]
"""
def setRowColZero(matrix,x,y):
    for i in range(len(matrix[x])):
        if matrix[x][i] != 0:
            matrix[x][i] = 0.1
    for i,arr in enumerate(matrix):
        if arr[y] != 0:
            matrix[i][y] = 0.1
    return matrix
    
def setMatZero(matrix):
    for i,line in enumerate(matrix):
        for j,item in enumerate(line):
            if item == 0:
                matrix = setRowColZero(matrix,i,j)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0.1:
                matrix[i][j] = 0
    return matrix

print(setMatZero([
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]))