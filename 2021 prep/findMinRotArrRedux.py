def minRotArrInner(nums, l, r, returnIndex):
    if nums[l] <= nums[r]:
        if returnIndex:
            return l
        return nums[l]
    mid = l+((r-l)//2)
    if nums[mid] >= nums[l]:
        return minRotArrInner(nums, mid+1, r, returnIndex)
    return minRotArrInner(nums, l, mid, returnIndex)


def minRotArr(nums, returnIndex=False):
    return minRotArrInner(nums, 0, len(nums)-1, returnIndex)


def binSearch(nums, target, l, r):
    mid = l+((r-l)//2)
    print(l, r, mid)
    if r == -1:
        return -1
    if nums[mid] == target:
        print("nums mid:", nums[mid])
        return mid
    if l >= r:
        print("res")
        return -1
    if nums[mid] >= target:
        return binSearch(nums, target, l, mid)
    return binSearch(nums, target, mid+1, r)


def searchMinRotArr(nums, target):
    print()
    if len(nums) <= 1:
        try:
            return nums.index(target)
        except:
            return -1
    minIndex = minRotArr(nums, True)
    if target <= nums[-1]:
        print('bin searching less', nums[minIndex:])
        return binSearch(nums[minIndex:], target, 0, len(nums)-1-minIndex)+minIndex
    print('bin searching', nums[0:minIndex])
    return binSearch(nums[0:minIndex], target, 0, minIndex-1)


"""
print(searchMinRotArr([4, 5, 6, 7, 0, 1, 2], 0))
print(searchMinRotArr([4, 5, 6, 7, 0, 1, 2], 3))
print(searchMinRotArr([1], 1))
"""
print(searchMinRotArr([3, 1], 0))
