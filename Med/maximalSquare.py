"""
Given a 2D binary matrix filled with 0's and 1's, find the 
largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
def maxSquareDP(matrix):
    if not matrix:
        return 0
    dp = []
    for x in range(0,len(matrix)):
        dp.append([])
        for y in range(0,len(matrix[x])):
            dp[x].append(0)
    currMax = 0
    for x in range(0,len(matrix)):
        for y in range(0,len(matrix[x])):
            print(matrix[x][y])
            if matrix[x][y] == "1":
                temp1 = 0
                temp2 = 0
                temp3 = 0
                if x>0:
                    temp1 = dp[x-1][y]
                if y>0:
                    temp2 = dp[x][y-1]
                if x>0 and y>0:
                    temp3 = dp[x-1][y-1]
                dp[x][y] = min(temp1,temp2,temp3)+1
                print(dp[x][y])
                if dp[x][y] > currMax:
                    currMax = dp[x][y]
    print(dp)
    return currMax*currMax
print(maxSquareDP([["1","0","1","0","0"],
                   ["1","0","1","1","1"],
                   ["1","1","1","1","1"],
                   ["1","0","0","1","0"]]))