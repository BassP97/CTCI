"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions 
as you like (ie, buy one and sell one share of the stock multiple times) with the 
following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock 
before you buy again).

After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""


def recWrapper(stocks):
    return recursiveSol(stocks, 'buy', 0)


def recursiveSol(stocks, currStatus, boughtPrice):
    if stocks == []:
        return 0
    if currStatus == 'buy':
        return max(recursiveSol(stocks[1:], 'buy', 0), recursiveSol(stocks[1:], 'sell', stocks[0]))
    if currStatus == 'sell':
        return max(recursiveSol(stocks[1:], 'sell', boughtPrice), recursiveSol(stocks[1:], 'cooldown', 0)+(stocks[0]-boughtPrice))
    else:
        return recursiveSol(stocks[1:], 'buy', 0)
