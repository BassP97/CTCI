"""
Given a set of non-overlapping intervals, insert a new interval 
into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according 
to their start times.

Example 1:

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
def insertInterval(intervals, newInterval):
    if intervals == []:
        return[newInterval]
    temp = len(intervals)
    for i,interval in enumerate(intervals):
        if interval[0]>=newInterval[0]:
            intervals.insert(i,newInterval)
            break
    if len(intervals) == temp:
        intervals.append(newInterval)
    i = 0
    while True:
        if i+1 >= len(intervals):
            break
        if intervals[i][1]>=intervals[i+1][0]:
            if intervals[i][1]<=intervals[i+1][1]:
                intervals[i][1] = intervals[i+1][1]
            del intervals[i+1]
        else:
            i = i+1
    print(intervals)
    return intervals
assert(insertInterval([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]])
assert(insertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]])
assert(insertInterval([[1,5]],[2,7]) == [[1,7]])