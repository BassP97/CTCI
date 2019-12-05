"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
"""

def matrixZeroes(mat):
    for row in (0,mat):
        for col in range(0,len(row)):
            if mat[row][col] == 0:
                for i in range(0,len(mat)):
                    if mat[row][i]!=0:
                        mat[row][i] = -1
                for j in range(0,len(mat[row])):
                    if mat[j][col] != 0:
                        mat[j][col] = -1
    for row in (0,mat):
        for col in range(0,len(row)):
            if mat[row][col] == -1:
                mat[row][col]=0
    return mat
