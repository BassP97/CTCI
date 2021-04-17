from collections import deque


def quickSelect(nums, k):
    res = nums
    pivotIndex = 0
    currIndex = 1
    while currIndex < len(res):
        if res[currIndex][1] < res[pivotIndex][1]:
            res.appendleft(res[currIndex])
            pivotIndex += 1
        else:
            currIndex += 1
    if pivotIndex == k:
        return res[pivotIndex:]
    if pivotIndex < k:
        return quickSelect(res[pivotIndex:], k)
    return quickSelect(res[:pivotIndex], k-pivotIndex)+list(res[pivotIndex:])


def kMostFrequent(nums, k):
    print("new:", nums)
    seenNums = []
    timesSeen = {}
    timesSeenToNum = {}
    frequencyArr = []
    for num in nums:
        if num not in timesSeen.keys():
            timesSeen[num] = 0
            seenNums.append(num)
        timesSeen[num] += 1
    print(timesSeen)
    for num in seenNums:
        if timesSeen[num] not in timesSeenToNum.keys():
            timesSeenToNum[timesSeen[num]] = []
        timesSeenToNum[timesSeen[num]].append(num)
        frequencyArr.append((timesSeen[num], num))
    return quickSelect(frequencyArr, k)


assert(kMostFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2])
assert(kMostFrequent([1], 1) == [1])
assert(kMostFrequent([3, 0, 1, 0], 1) == [0])
