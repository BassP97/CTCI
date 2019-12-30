"""
You decide to test if your oddly-mathematical heating company is fulfilling its 
All-Time Max, Min, Mean and Mode Temperature Guarantee™.

Write a class TempTracker with these methods:

    insert()—records a new temperature
    get_max()—returns the highest temp we've seen so far
    get_min()—returns the lowest temp we've seen so far
    get_mean()—returns the mean of all temps we've seen so far
    get_mode()—returns a mode of all temps we've seen so far

Optimize for space and time. Favor speeding up the getter methods get_max(), 
get_min(), get_mean(), and get_mode() over speeding up the insert() method.

get_mean() should return a float, but the rest of the getter methods can return 
integers. Temperatures will all be inserted as integers. We'll record our 
temperatures in Fahrenheit, so we can assume they'll all be in the range 0...110

If there is more than one mode, return any of the modes.
"""

class tempTracker(object):
    def __init__(self):
        self.max = 0
        self.min = 110
        self.mean = 0
        self.mode = 0
        self.modeCount = 0
        self.itemCount = {}
        self.numItems = []
    def insert(self, num):
        if num>self.max:
            self.max = num
        if num<self.min:
            self.min = num
        self.numItems.append(num)
        if num not in self.itemCount.keys():
            self.itemCount[num] = 0
        self.numItems = self.numItems+1
        self.itemCount[num] = self.itemCount[num]+1
        if len(self.numItems) == 1:
            self.mean = num
            self.mode = num
            return
        self.mean = ((self.mean*(self.numItems)-1)) + num)/self.numItems)
        if self.mode == num:
            self.modeCount = self.modeCount+1
        if self.itemCount[num]>self.modeCount:
            self.mode = num
            self.modeCount = self.itemCount[num]
        return
    def get_max(self):
        return self.max
    def get_mean(self):
        return self.mean
    def get_min(self):
        return self.min
    def get_mode(self):
        return self.mode
    