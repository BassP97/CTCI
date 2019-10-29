"""
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.

"""

#we iterate through rows until we undershoot - then we iterate through the row to find our target or something greater than
#our target - at which point we drop another row and iterate again

#we can do this because, if our current item is greater than our target, we know that all above previous rows are full of 
#items that are less than our target - when we drop a level we'll either drop to our target(in which case we stop)
#or an item less than our target, at which point we repeat this process

def alternateSol(arr, target):
    row = len(arr)-1
    column = 0
    while row>=0 and column < len(arr[0]):
        if arr[row][column] == target:
            return True
        if arr[row][column] > target:
            row = row-1
        else:
            column = column+1
    return False

