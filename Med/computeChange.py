"""
Your quirky boss collects rare, old coins. They found out you're a programmer 
and asked you to solve something they've been wondering for a long time.

Write a function that, given:

    an amount of money
    a list of coin denominations

computes the number of ways to make the amount of money with coins of the 
available denominations.

Example: for amount=4 and denominations=[1,2,3], your program would output 
4—the number of ways to make 4¢ with those denominations:

    1¢, 1¢, 1¢, 1¢
    1¢, 1¢, 2¢
    1¢, 3¢
    2¢, 2¢

"""
import collections


def computeChange(total, coins):
    waysOfMakingN = [0]*(total+1)
    for i in range(0,total+1):
        temp = 0
        for coin in coins:
            if i-coin > 0:
                temp = temp+waysOfMakingN[i-coin]
            if i-coin == 0:
                temp = temp+1
        waysOfMakingN[i]=temp
    return waysOfMakingN[total-1]


print(computeChange(8, [1,2,3]))