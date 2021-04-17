"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in-place.
"""

def tagColumn(row, column, matrix):
    for i in matrix:
        if i!=0:
            i[column] = -1

def tagRow(row, column, matrix):
    for i in range(0,len(matrix[row])):
        if matrix[row][i]!=0:
            matrix[row][i] = -1

def zeroColumn(row, column, matrix):
    for i in matrix:
        i[column] = 0

def zeroRow(row, column, matrix):
    for i in range(0,len(matrix[row])):
        matrix[row][i] = 0

def showMatrix(matrix):
    for i in matrix:
        print i
    print ""
#note - assumes that the matrix only contains non zero elements
def zeroMatrix(matrix):
    for row in range(0,len(matrix)):
        for column in range(0,len(matrix[row])):
            if matrix[row][column] == 0:
                tagColumn(row, column, matrix)
                tagRow(row, column, matrix)
    for row in range(0,len(matrix)):
        for column in range(0,len(matrix[row])):
            if matrix[row][column] == -1:
                matrix[row][column]=0
    showMatrix(matrix)
    return matrix

#works w/ non zero elements too!
def betterSolution(matrix):
    for row in range(0,len(matrix)):
        for column in range(0,len(matrix[row])):
            if matrix[row][column] == 0:
                matrix[row][0] = 0
                matrix[0][column] = 0
                matrix[row][column] = 1
    showMatrix(matrix)
    for column in range(0,len(matrix[0])):
        if matrix[0][column] == 0:
            zeroColumn(0,column,matrix)
    showMatrix(matrix)

    for rowStart in range(0,len(matrix)):
        if matrix[rowStart][0] == 0:
            zeroRow(rowStart,0,matrix)
    showMatrix(matrix)

"""zeroMatrix([
  [1,1,1],
  [1,0,1],
  [1,1,1]
])"""

betterSolution([
  [1,1,1],
  [1,0,1],
  [1,1,1]
])
