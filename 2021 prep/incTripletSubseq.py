"""
Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Example 1:
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.

Example 2:
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.

Example 3:
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.



Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1


[2,1,2,0,3]
"""

"""
takeaway:
always think about ways that the *last* element of a given sequence can store information about 
said sequence. In this instance, if we encounter a new potential "first", we store it in "first"
However, in cases like [2,1,2,0,3], this "first" item does not actually model the first item in
the sequence we return. In these cases, we rely upon the "second" element to store the 
"second" item in the prior candidate sequence - if we encounter something greater than this "second"
item, we know it's by extension greater than the first item in the prior candidate sequence, and
can thus return true. If we encounter a number that is smaller than this "second" item, we know
the prior candidate sequence is now moot (since if i<j<k, and some new item o<j, i<o<k as well)
"""


def tripletSubseq(nums):
    first = float('inf')
    # this stores either the second element in the current subsequence, OR the second element in the "prior" subsequence
    second = float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False
