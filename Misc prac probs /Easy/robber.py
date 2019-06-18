"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you
from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
"""

def main(toCheck):
    totalEven = 0
    totalOdd = 0
    for i in range(0,len(toCheck)):
        if i%2 == 0:
            totalEven = totalEven + toCheck[i]
        else:
            totalOdd = totalOdd + toCheck[i]
    return max(totalEven, totalOdd)



assert(main([1,2,3,1]) == 4)
assert(main([2,7,9,3,1]) == 12)
