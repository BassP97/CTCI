"""
Given an array with n objects colored red, white or blue, sort them in-place so
that objects of the same color are adjacent, with the colors in the order red,
white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

def sortColors(colorList):
    colorZero = []
    colorOne = []
    colorTwo = []
    for i in colorList:
        if i == 0:
            colorZero.append(0)
        elif i == 1:
            colorOne.append(1)
        elif i == 2:
            colorTwo.append(2)
    print (colorZero, colorOne, colorTwo)
    retArr = colorZero+colorOne+colorTwo
    print(retArr)
    return retArr

def swap(arr,indexOne,indexTwo):
    temp = arr[indexOne]
    arr[indexOne] = arr[indexTwo]
    arr[indexTwo] = temp
    return

#in place sort, called the dutch flag sort
def dutchFlagSort(colorList):
    mid = 1
    lo = 0
    mi = 0
    hi = len(colorList)-1

    while mi<=hi:
        if colorList[mi]<mid:
            swap(colorList, lo, mi)
            mi = mi+1
            lo = lo+1
        elif colorList[mi]>mid:
            swap(colorList, mi, hi)
            hi = hi-1
        else:
            mi = mi+1
    return colorList

assert(sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2])
assert(dutchFlagSort([2,0,2,1,1,0]) == [0,0,1,1,2,2])
