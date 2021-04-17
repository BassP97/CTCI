"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.
"""

def mergeArr(arr1,arr2):
    retArr = []
    m = 0
    n = 0

    while(n != len(arr1) and m != len(arr2)):
        if arr1[n]>arr2[m]:
            retArr.append(arr2[m])
            m = m+1
        else:
            retArr.append(arr1[n])
            n = n+1
        print(retArr)
    if n != len(arr1):
        for i in range(n,len(arr1)):
            retArr.append(arr1[i])
    elif m != len(arr2):
        for i in range(m,len(arr2)):
            retArr.append(arr2[i])
    print(retArr)
    return retArr

mergeArr([0,1,5,6,8,12,15,67], [9,14,56,77,89])
