"""
You are given an integer array nums sorted in
ascending order (with distinct values), and an integer target.

Suppose that nums is rotated at some pivot unknown
to you beforehand (i.e., [0,1,2,4,5,6,7] might become
[5,6,7,0,1,2,4]).

If target is found in the array return its index, otherwise, return -1.


"""
import time


def findPivot(arr, l, r):
    time.sleep(0.2)
    mid = l+((r-l)//2)
    print(arr, l, r, mid)
    if (mid == 0) or (mid == len(arr)-1) or (arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]):
        return mid
    print(arr[mid], arr[l], arr[r])
    if arr[mid] >= arr[l] and arr[mid] > arr[r]:
        print("searching right")
        return findPivot(arr, mid+1, r)
    return findPivot(arr, l, mid)


def searchWrapper(arr, target):
    return searchRotatedArr(arr, 0, len(arr)-1, target)


def binSearch(arr, l, r, target):
    mid = l+((r-l)//2)
    if arr[mid] == target:
        return mid
    if l >= r:
        return -1
    if target < arr[mid]:
        return binSearch(arr, l, mid-1, target)
    return binSearch(arr, mid+1, r, target)


def searchRotatedArr(arr, l, r, target):
    if len(arr) <= 2:
        if target in arr:
            return arr.index(target)
        return -1
    midPoint = findPivot(arr, l, r)
    print(midPoint)
    if target == arr[0]:
        return 0
    if target < arr[0] or arr[l] < arr[r]:
        return binSearch(arr, midPoint, len(arr)-1, target)
    return binSearch(arr, 0, midPoint-1, target)


assert(searchWrapper([5, 6, 7, 0, 1, 2, 4], 6) == 1)
assert(searchWrapper([5, 6, 7, 0, 1, 2, 4], 0) == 3)
assert(searchWrapper([0, 1, 2, 4, 5, 6, 7], 5) == 4)
assert(searchWrapper([4, 5, 6, 7, 0, 1, 2], 0) == 4)
assert(searchWrapper([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4)
assert(searchWrapper([5, 1, 2, 3, 4], 1) == 1)
assert(searchWrapper([3, 1], 1) == 1)
assert(searchWrapper([3, 5, 1], 0) == -1)
assert(searchWrapper([2, 3, 4, 5, 6, 7, 8, 1], 3) == 1)
