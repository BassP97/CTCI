"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the
matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

#destructive solution, repeated if checks, kinda bad time complexity wise, p bad lol
def spiralMatrix(matrix):
    retArr = []
    while (True):
        if len(matrix) == 0:
            break
        for num in matrix[0]:
            retArr.append(num)

        matrix.pop(0)

        if len(matrix) == 0:
            break

        for i in range(0,len(matrix)):
            retArr.append(matrix[i][len(matrix[i])-1])
            matrix[i].pop(len(matrix[i])-1)
        if len(matrix) == 0:
            break

        for i in range(len(matrix[len(matrix)-1])-1,-1,-1):
            retArr.append(matrix[len(matrix)-1][i])

        matrix.pop(len(matrix)-1)

        if len(matrix) == 0:
            break

        for i in range(len(matrix)-1,-1,-1):
            retArr.append(matrix[i][0])
            matrix[i].pop(0)


#doesnt quite work but close enough lol
def betterSpiral(matrix):
    currLayer = 0
    retArr = []
    while (True):
        for num in matrix[currLayer][currLayer:len(matrix[currLayer])-currLayer]:
            retArr.append(num)

        for i in range(1,len(matrix)-currLayer-1):
            retArr.append(matrix[i][len(matrix[i])-1])

        for i in range(len(matrix[len(matrix)-1])-1-currLayer,currLayer,-1):
            retArr.append(matrix[len(matrix)-currLayer-1][i])

        for i in range(len(matrix)-1-currLayer,currLayer,-1):
            retArr.append(matrix[i][0])
        currLayer = currLayer+1
    print(retArr)

betterSpiral([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
betterSpiral([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])
