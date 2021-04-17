"""
You are climbing a stair case.
It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
"""

def main(numSteps):
    steps = [1,2]
    #one can reach the ith step from either the i-1th step or the i-2th step
    #thus, the number of ways to reach the ith step is equal to the number of ways
    #to get to the i-1th step plus the number of ways to reach the i-2th step
    for i in range(2,numSteps):
        steps.append(steps[i-1]+steps[i-2])
    return steps[numSteps-1]


assert(main(2) == 2)
assert(main(3)==3)
