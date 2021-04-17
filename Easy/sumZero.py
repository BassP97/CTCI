"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""

def sumZero(k):
    arr = []
    if k%2==0:
        for i in range(0,len(k)/2):
            arr.append(i)
        for i in range(0,len(k)/2):
            arr.append(0-i)
    else:
        arr.append(0)
        temp = k-1
        for i in range(0,len(temp)/2):
            arr.append(i)
        for i in range(0,len(temp)/2):
            arr.append(0-i)
    return arr