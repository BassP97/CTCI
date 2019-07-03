"""
Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible
order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding
outputs are in the right-hand column.
"""
def swap(i,j,swapArr):
    temp = swapArr[i]
    swapArr[i] = swapArr[j]
    swapArr[j] = temp
    return swapArr

"""
Algorithm:
keep reducing problem size by removing the most significant digit until either
our list of numbers is one digit long, or the given section is as large as possible

Then sort that largest section of the list, thus making it as small as it can be

Then, take the smallest digit from the sorted subsection and swap it with the next
largest digit. Then, return all the way up the chain!
"""
def main(toPermute):
    #already the largest possible value
    if (sorted(toPermute, reverse = True) == toPermute) or len(toPermute) == 1:
        return sorted(toPermute)
    toReturn = main(toPermute[1:])
    sortCheck = sorted(toReturn)
    if (toReturn == sortCheck):
        toReturn = swap(0,1,toPermute)
    else:
        toReturn.insert(0,toPermute[0])
    print(toReturn)
    return toReturn
main([1,2,3])
assert(main([1,2,3])==[1,3,2])
assert(main([3,2,1])==[1,2,3])
assert(main([1,1,5])==[1,5,1])
