"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4


"""


def quickSelect(nums, k):

    print(nums, k)
    pivot = nums[0]
    leftHalf = []
    rightHalf = []
    for num in nums[1:]:
        if num < pivot:
            leftHalf.append(num)
        else:
            rightHalf.append(num)
    if len(rightHalf) == k-1:
        return pivot
    if len(rightHalf) > k-1:
        return quickSelect(rightHalf, k)
    return quickSelect(leftHalf, k-len(rightHalf)-1)


def simpleSol(nums, k):
    return sorted(nums)[len(nums)-k]


#assert(simpleSol([2, 1], 2) == quickSelect([2, 1], 2))
assert(quickSelect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
       == simpleSol([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
