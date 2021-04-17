"""
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


def first(n):
    return n[0]


def canMerge(interval1, interval2):
    return interval2[0] <= interval1[1]


def mergeIntervals(intervals):
    if len(intervals) == 0:
        return []
    sortedIntervals = sorted(intervals, key=first)
    finalIntervals = []
    i = 0
    currInterval = sortedIntervals[0]
    while i < len(sortedIntervals):
        if canMerge(currInterval, sortedIntervals[i]):
            currInterval[1] = max(sortedIntervals[i][1], currInterval[1])
        else:
            finalIntervals.append(currInterval)
            currInterval = sortedIntervals[i]
        i += 1
    finalIntervals.append(currInterval)
    return finalIntervals


assert(mergeIntervals([[1, 4], [4, 5]]) == [[1, 5]])
assert(mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]])
       == [[1, 6], [8, 10], [15, 18]])
