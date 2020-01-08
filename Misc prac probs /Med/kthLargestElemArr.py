"""
Find the kth largest element in an unsorted array. Note that it 
is the kth largest element in the sorted order, not the kth distinct element.
"""

def kthElemArr(nums,k):
    kArr = []
    for num in nums:
        if len(kArr)==k:
            for i in range(0,len(kArr)):
                if num>k:
                    kArr[i] = num
                    break
        else:
            kArr.append(num)
    return min(nums)

def kthElemQuickselect(nums,k):
    pivot = nums[0]
    lowerList = []
    upperList = []
    equalList = []
    print(nums,k)
    for num in nums:
        if num<pivot:
            lowerList.append(num)
        elif num>pivot:
            upperList.append(num)
        else:
            equalList.append(num)
    if k<=len(upperList):
        return kthElemQuickselect(upperList,k)
    if k-len(upperList)-len(equalList)>=0:
        return pivot
    if k > len(upperList):
        return kthElemQuickselect(lowerList, k-len(upperList)-len(equalList))


print(kthElemQuickselect([3,2,3,1,2,4,5,5,6],4))
        

