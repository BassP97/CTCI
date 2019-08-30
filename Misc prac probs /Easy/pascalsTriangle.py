"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

def pascals(numRows):
    triangle = [[1]]
    for i in range(1,numRows):
        currRow = []
        currRow.append(1)
        for j in range(0,len(triangle[i-1])-1):
            currRow.append(triangle[i-1][j]+triangle[i-1][j+1])
        currRow.append(1)
        triangle.append(currRow)
    for i in triangle:
        print (i)
    return triangle

assert(pascals(5) == [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
])
pascals(9)
