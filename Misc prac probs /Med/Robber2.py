"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
def main(toRob):
    even = 0
    odd = 0
    for i in range(0,len(toRob)):
        if (i%2 == 0):
            even = even+toRob[i]
        else:
            odd = odd+toRob[i]
        print(even,odd)
    if len(toRob)%2 != 0:
        even = max(even-toRob[-1], even-toRob[0])
    return max(even,odd)

assert(main([1,2,3,1]) == 4)
assert(main([2,3,2]) == 3)
