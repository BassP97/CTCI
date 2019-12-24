"""
Find a duplicate, Space Edition™.

We have a list of integers, where:

    The integers are in the range 1..n
    The list has a length of n+1

It follows that our list has at least one integer which 
appears at least twice. But it may have several duplicates, 
and each duplicate may appear more than twice.

Write a function which finds an integer that appears more 
than once in our list. (If there are multiple duplicates, 
you only need to find one of them.)


do this in O(1) time without destroying original input
"""

#we can do this using floyd's algorithm to detect a cycle treat input as kind of pointer, where given num indicates next 
#location to visit in the array. Use floyd's, and then find where the cycle starts to get duplicate
#there's a math proof about finding start of cycle that you probably don't need to remember
#see your green notebook with the mushrooms on the cover for the proof - it has to do with the relationship between
#cycle length and the "lead in" length before the cycle. 
def cycleStart(arr, meetLoc):
    start = arr[0]
    while start!=meetLoc:
        start = arr[start]
        meetLoc = arr[meetLoc]
    return start

def spaceDupicate(arr):
    tortoise = arr[0]
    hare = arr[0]
    while True:
        tortoise = arr[tortoise]
        hare = arr[hare]
        hare = arr[hare]
        if tortoise == hare:
            return cycleStart(arr, tortoise)

print(spaceDupicate([1,6,2,7,3,9,8,4,5,2]))