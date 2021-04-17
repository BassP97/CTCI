"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a
non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned.
"""
import time

#note - assumes that the input has an integer square root
def sqrt(num):
    right = num
    left = 0
    while True:
        mid = left + (left+right)//2
        if mid*mid>num:
            right = mid-1
        else:
            if mid*mid == num:
                return mid
            else:
                left = mid+1
    print(mid)
    return sqrt

print(sqrt(4))
print(sqrt(81))
print(sqrt(1024))
