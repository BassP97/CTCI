def climbStairs(stairCount):
    if stairCount == 1:
        return 1
    if stairCount == 2:
        return 2
    res = [0 for i in range(stairCount)]
    res[0] = 1
    res[1] = 2
    for i in range(2, stairCount):
        res[i] = res[i-1]+res[i-2]
    return res[-1]
