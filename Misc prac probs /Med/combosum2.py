import copy

def comboSum(candidates,target):
    dp = []
    for i in range(target+1):
        dp.append([])
    for i,num in enumerate(candidates):
        if num<len(dp):
            dp[num].append([num])
    seenIt = set()
    for i in range(len(dp)):
        for loc,num in enumerate(candidates):
            if i-num>0 and len(dp[i-num])>0:
                temp = copy.deepcopy(dp[i-num])
                for k in range(len(temp)):
                    temp[k].append(num)
                    temp[k].sort()
                    if tuple(temp[k]) not in seenIt:
                        seenIt.add(tuple(temp[k]))
                        dp[i].append(temp[k])
    return dp[target]