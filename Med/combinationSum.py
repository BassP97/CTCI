"""
Given an integer array with all positive numbers and 
no duplicates, find the number of possible combinations 
that add up to a positive integer target.
"""

def getInput():
    input()
    menu = [int(i) for i in input().split(' ')]
    input()
    orders = [int(i) for i in input().split(' ')]
    return menu, orders

def comboSum(candidates,target):
    targetDict = {}
    dp = [1]+[0]*target
    for i,num in enumerate(candidates):
        dp[num]+=1
        targetDict[num] = [i+1]
    seenIt = set()
    for i in range(len(dp)):
        for itemIndex,num in enumerate(candidates):
            if i-num>0 and dp[i-num]>0:
                tempSet = tuple(sorted(targetDict[i-num]+[itemIndex+1]))
                if tempSet not in seenIt:
                    seenIt.add(tempSet)
                    dp[i] = dp[i]+dp[i-num]
                    if i not in targetDict.keys():
                        targetDict[i] = targetDict[i-num] + [itemIndex+1]
                        targetDict[i].sort()
    if dp[target]==1:
        listUtil(targetDict[target])
        return
    if dp[target]==0:
        print('Impossible')
        return
    print('Ambiguous')
    return
    
def listUtil(listInput):
    for item in listInput:
        print(item, end = ' ')
    print()
    
def main():
    menu, orders = getInput()
    for order in orders:
        comboSum(menu, order)
main()