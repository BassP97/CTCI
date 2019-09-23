"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
elements are subset of nums2. Find all the next greater numbers for nums1's elements

The Next Greater Number of a number x in nums1 is the first greater number to
its right in nums2. If it does not exist, output -1 for this number.
"""
def binSearch(toFind, arr, start, end):
    mid = (start+end)//2
    print(toFind,start,mid,end)
    if arr[mid] == toFind:
        print("returning mid")
        return mid
    elif arr[mid] != toFind:
        if arr[mid]<toFind:
            return binSearch(toFind, arr, mid+1, end)
        if arr[mid]>toFind:
            return binSearch(toFind, arr, 0, mid-1)

def nge(num1,num2):
    num2.sort()
    retArr = []
    print (num2)
    for num in num1:
        temp = binSearch(num,num2,0,len(num2))
        print (temp)
        if temp<len(num2)-1:
            retArr.append(num2[temp+1])
            print(retArr)
        else:
            retArr.append(-1)
    print (retArr)
    return retArr


assert(nge([4,1,2], [1,3,4,2]) == [-1,2,2])
