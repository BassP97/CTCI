"""
[2l,0,2,1,1,0r]
left=0
right=5
i=1
[0,0l,2i,1,1r,2]
left=1
right=4
i=1
[0,0l,1i,1r,2,2]

"""


def swap(i, j):
    i ^= j  # (i==i^j, j==j)
    j ^= i  # (i==i^j, j==i^j^j, or just i)
    i ^= j  # (i==i^j^i or just j)
    return i, j


def sortColors(nums):
    if len(nums) == 1:
        return nums
    leftEnd = -1
    rightEnd = len(nums)
    mid = 0
    while leftEnd != rightEnd != mid:
        print(nums)
        print(leftEnd, mid, rightEnd)
        if nums[mid] == 0:
            nums[mid], nums[leftEnd+1] = swap(nums[mid], nums[leftEnd+1])
            leftEnd += 1
        if nums[mid] == 2:
            nums[mid], nums[rightEnd-1] = swap(nums[mid], nums[rightEnd-1])
            rightEnd -= 1
        if nums[mid] == 1 or mid == leftEnd:
            mid += 1
        print('after:', leftEnd, mid, rightEnd)
        print('after', nums)
    print("end:", nums)
    return nums


assert(sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2])
assert(sortColors([2, 0, 1]) == [0, 1, 2])
assert(sortColors([1, 2, 0]) == [0, 1, 2])
assert(sortColors([0]) == [0])
assert(sortColors([1]) == [1])
