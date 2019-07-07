"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""

def main(sortedArr, toFind, min, max):
    if sortedArr[(min+max)//2] == toFind:
        left = ((min+max)//2)-1
        right = ((min+max)//2)+1
        totalFound = 1
        leftFound = False
        rightFound = False
        while True:
            if left >= 0 and (not leftFound):
                if sortedArr[left] != toFind:
                    left = left + 1
                    leftFound = True
                else:
                    left = left-1
            if right <= len(sortedArr)-1 and (not rightFound):
                if sortedArr[right] != toFind:
                    right = right - 1
                    rightFound = True
                else:
                    right = right + 1
            if rightFound and leftFound:
                break;
        print(left,right)
        return [left,right]
    elif min == max:
        return [-1,-1]
    else:
        if sortedArr[(min+max)//2]<toFind:
            return(main(sortedArr,toFind,((min+max)//2)+1, max))
        else:
            return(main(sortedArr,toFind, min, ((min+max)//2)-1))





assert(main([5,7,7,8,8,10], 8, 0, 5) == [3,4])
assert(main([5,7,7,8,8,10], 6, 0, 5) == [-1,-1])
print("done!")
