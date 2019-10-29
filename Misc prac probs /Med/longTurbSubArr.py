"""
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

    For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
    OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.

That is, the subarray is turbulent if the comparison sign flips between each adjacent 
pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.
"""

def longTurbSubArr(arr):
    left1 = 0
    left2 = 0
    right1 = 0
    right2 = 0
    currIndex = 0 
    currMax = 0
    while currIndex < len(arr):
        if arr[currIndex]%2 == 0:
            if arr[currIndex]<arr[currIndex+1]:
                left2 = currIndex
                right2 = currIndex
                right1 = right1+1
            else:
                left1 = currIndex
                right1 = currIndex
                right2 = right2+1
        else:
            if arr[currIndex]<arr[currIndex+1]:
                left1 = currIndex
                right1 = currIndex
                right2 = right2+1
            else:
                left2 = currIndex
                right2 = currIndex
                right1 = right1+1
        if right1-left1>currMax:
            currMax = right1-left1
        if righ2-left2>currMax:
            currMax = right2-left2
    return currMax
        

