"""
The i-th person has weight people[i], and each boat can carry a maximum 
weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of 
the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is 
guaranteed each person can be carried by a boat.)

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
"""


#can heaviest share with lightest? if so, make em share. Else, give heaviest own boat
def boatPeople(people, limit):
    boats = 0
    people.sort()
    i = 0
    j = len(people)-1
    while i<j:
        print(i,j)
        if people[i]+people[j]<=limit:
            i = i+1
            j = j-1
        else:
            j = j-1
        boats = boats+1
    if i == j:
        boats = boats+1
    return boats


print(boatPeople([1,2],3))
print(boatPeople([3,2,2,1],3))
print(" ")
print(boatPeople([2,4],5))