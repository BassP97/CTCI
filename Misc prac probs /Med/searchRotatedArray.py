"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""
def main(toCheck, target):
    if (len(toCheck) == 1):
        if target == toCheck[0]:
            return 0
        return -1
    left = 0
    right = len(toCheck)-1
    mid = (left+right)//2
    found = False
    while True:
        print(left,right)
        if toCheck[mid] > toCheck[left] and target < toCheck[left]:
            left = mid
        elif(toCheck[mid]>toCheck[left] and target>toCheck[left]):
            right = mid
        elif toCheck[mid]<toCheck[left] and target<toCheck[left]:
            left = mid
        elif toCheck[mid]<toCheck[left] and target>toCheck[left]:
            right = mid
        if(toCheck[mid] == target):
            return mid
        mid = (left+right)//2

        if mid == left or mid == right:
            break;
    return -1


assert(main([4,5,6,7,0,1,2],0) == 4)
assert(main([4,5,6,7,0,1,2],3) == -1)
