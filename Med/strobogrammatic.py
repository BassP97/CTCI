"""
A strobogrammatic number is a number that looks the 
same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is 
strobogrammatic. The number is represented as a string.
For example, the numbers "69", "88", and "818" are all strobogrammatic.

------Notes------
-Any number of 1s or 8s flanked by any of the following is strobogrammatic
-A 'strobo-palindromic' series of 6s and 9s is strobogrammatic, where strobo-palindromic refers to a 6 being the palindromic equivelant of a 9 and vice versa
-A true-palindromic series of 8s is strobogrammatic
-A true-palindromic series of 1s is strobogrammatic
-Any combination of the above rules is also valid - so 6181819 is strobogrammmatic

-So, our algorithm will check the following:
    - 
"""
def strobo(num):
