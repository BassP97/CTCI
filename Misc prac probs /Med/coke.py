import collections
import copy
def getInput():
    numTests = int(input())
    cokes = []
    coins = []
    for i in range(numTests):
        totalInput = [int(i) for i in input().split(' ')]
        coins.append(totalInput[1:])
        cokes.append(totalInput[0])
    return coins, cokes

def computeChange(numCokes, coins):
    coinVals = [1,5,10]
    coinsAtLoc = {}
    coinsAtLoc[0] = copy.deepcopy(coins)
    cokeArr = [0]*((numCokes*8)+1)
    for i in range(1,len(cokeArr)):
        options = []
        for j,coin in enumerate(coinVals):
            if i-coin>=0 and i-coin in coinsAtLoc.keys():
                if coinsAtLoc[i-coin][j] > 0:
                    temp = copy.deepcopy(coinsAtLoc[i-coin])
                    temp[j]-=1
                    options.append(temp)
        if options != []:
            minCoins = float('inf')
            toAppend = []
            for option in options:
                if sum(option)<minCoins:
                    toAppend = option
                    minCoins = sum(option)
            coinsAtLoc[i] = toAppend
            cokeArr[i] = sum(coins)-minCoins
    print(cokeArr)
    return sum(coins)-sum(coinsAtLoc[numCokes])

def main():
    coins,cokes = getInput()
    for coin,coke in zip(coins,cokes):
        print(computeChange(coke, coin))
main()