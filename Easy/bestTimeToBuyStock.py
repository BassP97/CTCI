"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell 
one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""
import sys

def buySellStock(prices):
    if prices == []:
        return 0
    lowest = prices[0]
    currMax = 0
    for price in prices:
        if price < lowest:
            lowest = price
            highest = 0
        if price-lowest > currMax:
            currMax = price-lowest
    return currMax

print(buySellStock([7,6,4,3,1]))     
