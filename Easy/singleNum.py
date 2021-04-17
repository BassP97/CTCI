"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.
"""

#good time complexity but takes O(n) space
def main(toCheck):
    setNums = {}
    for i in toCheck:
        if i in setNums.keys():
            setNums[i] = True
        else:
            setNums[i] = False
    for key in setNums.keys():
        if setNums[key] == False:
            return key

#linear time, O(1) space
#note that set(blah) eliminates all duplicates from blah
#so for an input of [a,a,b,b,c] we get: 2*(a+b+c)−(a+a+b+b+c) which equals C
def mathFam(toCheck):
    return 2*sum(set(toCheck)) - sum(nums)


assert(main([2,2,1]) == 1)
assert(main([4,1,2,1,2]) == 4)
