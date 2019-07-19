"""
Given a set of distinct integers, nums, return all possible
subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""

def findPowSet(set):
    powSet = []
    sizePowSet = 2**len(set)
    formatStr = '{0:0'+str(len(set))+'b}'
    for i in range(0, sizePowSet):
        entryInPowSet = []
        binStr = formatStr.format(i)
        for j in range(0,len(binStr)):
            if binStr[j] == "1":
                entryInPowSet.append(set[j])
        powSet.append(entryInPowSet)
    print(powSet)
    return powSet

findPowSet([0,1,2])
findPowSet([0,1,2,8,3,2,3,8,1,2,2,0,9,2,3,1,5,8])
