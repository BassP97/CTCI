"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
"""
def main(coins, toReach):
    prevReached = {0:0}
    smallestJump = 0
    for i in range(1, toReach+1):
        smallestJump = float('inf')
        for coin in coins:
            if i-coin >=0:
                if (i-coin in prevReached.keys()):
                    if prevReached[i-coin]<smallestJump:
                        smallestJump = prevReached[i-coin]
        if smallestJump!=float('inf'):
            prevReached.update({i: smallestJump+1})
    if toReach in prevReached.keys():
        return prevReached[toReach]
    return -1



assert(main([1, 2, 5], 11)==3)
assert(main([1, 7, 2], 15)==3)
assert(main([2, 8, 5], 23)==4)
