def buySell(prices):
    lo = float('inf')
    maxProfit = 0
    for price in prices:
        if price < lo:
            lo = price
        if price-lo > maxProfit:
            maxProfit = price-lo
    return maxProfit


print(buySell([7, 1, 5, 3, 6, 4]))
