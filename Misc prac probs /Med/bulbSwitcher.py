"""
There are n bulbs that are initially off. You first turn on all the bulbs.
Then, you turn off every second bulb. On the third round, you toggle every
third bulb (turning on if it's off or turning off if it's on). For the i-th
round, you toggle every i bulb. For the n-th round, you only toggle the last
bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1
Explanation:
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
"""

def bulbSwitch(bulbs, rounds):
    numOn = len(bulbs)
    for bulb in bulbs:
        bulb = True
    for i in range(0,len(bulbs)):
        for j in rounds:
            if ((i+1)%j)==0:
                bulbs[i] = not bulbs[i]
                if bulbs[i]:
                    numOn = numOn+1
                else:
                    numOn = numOn-1
    return numOn


#alternative = nth bulb's state is equal to the number of unique divisors it has
#under length <rounds>. Divisors always come in pairs if a number isn't a perfect square,
#for instance 12 has (1,12)(2,6)(3,4), so non perfect squares under n will always be the same state
#that they were at the start - on. Perfect squares will be in the opposite state - off

#so, let's just count the square numbers. We do this with square root of n because we know that
# n will be 1, 4, 9 ... n and its corresponding square roots will be 1, 2, 3... up to sqrt(n).

def bulbSwitchGood(bulbs, rounds):
    return sqrt(rounds)
