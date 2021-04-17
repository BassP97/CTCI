"""

"""


def uniquePaths(m, n):
    res = []
    for i in range(m):
        res.append([0 for j in range(n)])
    res[0][0] = 1
    print(res)
    for i in range(m):
        for j in range(n):
            above = 0
            toTheLeft = 0
            if i > 0:
                above = res[i-1][j]
            if j > 0:
                toTheLeft = res[i][j-1]
            res[i][j] = above+toTheLeft+res[i][j]
            print(i, j, res)
    print(res)
    return res[m-1][n-1]
