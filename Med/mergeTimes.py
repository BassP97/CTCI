"""
 Write a function merge_ranges() that takes a list of multiple meeting 
 time ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

  [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming 
from multiple teams.

Write a solution that's efficient even when we can't put a nice upper 
bound on the numbers representing our time ranges. Here we've simplified 
our times down to the number of 30-minute slots past 9:00 am. But we want 
the function to work even for very large numbers, like Unix timestamps. 
In any case, the spirit of the challenge is to merge meetings where 
start_time and end_time don't have an upper bound. 
"""
def mergeTimes(times):
    times.sort(key=lambda tup:tup[0])
    i = 0
    while True:
        if i >= len(times)-1:
            break
        if times[i][1]>=times[i+1][0]:
            times[i][1] = times[i+1][1]
            del times[i+1]
        else:
            i = i+1
    return times

print(mergeTimes([[0, 1], [3, 5], [4, 8], [10, 12], [9, 10]]))
