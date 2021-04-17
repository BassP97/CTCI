"""
You are given coins of different denominations and 
a total amount of money amount. Write a function 
to compute the fewest number of coins that you need 
to make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of 
each kind of coin.
"""


def coinChange(coins, toReach):
    if toReach == 0:
        return 0
    res = [0 for i in range(toReach+1)]
    for i in range(toReach+1):
        for coin in coins:
            if (i-coin > 0 and res[i-coin] > 0) or i-coin == 0:
                print("hit")
                if res[i] > 0:
                    res[i] = min(res[i], res[i-coin]+1)
                else:
                    res[i] = res[i-coin]+1
        print(res)
    if res[toReach] == 0:
        return -1
    return res[toReach]


assert(coinChange([1, 2, 5], 11) == 3)
assert(coinChange([2], 3) == -1)
assert(coinChange([1], 0) == 0)
assert(coinChange([1], 1) == 1)
assert(coinChange([1], 2) == 2)
