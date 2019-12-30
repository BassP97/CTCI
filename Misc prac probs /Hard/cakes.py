"""
You are a renowned thief who has recently switched from stealing 
precious metals to stealing cakes because of the insane profit margins. You end up 
hitting the jackpot, breaking into the world's largest privately owned stock of cakes—
the vault of the Queen of England.

While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.

Each type of cake has a weight and a value, stored in a tuple with two indices:

    An integer representing the weight of the cake in kilograms
    An integer representing the monetary value of the cake in British shillings

For example:

     # Weighs 7 kilograms and has a value of 160 shillings
    (7, 160)

    # Weighs 3 kilograms and has a value of 90 shillings
    (3, 90)

You brought a duffel bag that can hold limited weight, and you want to make off with the
 most valuable haul possible.

Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight 
capacity, and returns the maximum monetary value the duffel bag can hold.

For example:

    cake_tuples = [(7, 160), (3, 90), (2, 15)]
    capacity    = 20

# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
max_duffel_bag_value(cake_tuples, capacity)

Weights and values may be any non-negative integer. Yes, it's weird to think about cakes that 
weigh nothing or duffel bags that can't hold anything. But we're not just super mastermind 
criminals — we're also meticulous about keeping our algorithms flexible and comprehensive. 
"""
"""
def cakeCalculator(capacity, cakes):
    cakeQuality = [0]*len(cakes)
    for i in range(0,len(cakes)):
        if cakes[i][0] == 0 and cakes[i][1]>0:
            return float(inf)
        elif cakes[i][0] == 0:
            del cakes[i]
            continue
        else:
            ratio = cakes[i][1]/cakes[i][0]
            cakeQuality[i] = ratio
    sortedCakes = [x for _,x in sorted(zip(cakeQuality,cakes), reverse=True)]
    total = 0
    for cake in sortedCakes:
        if capacity == 0:
            break
        temp = capacity//cake[0]
        if temp > 0:
            capacity = capacity-(temp*cake[0])
            total = total+(temp*cake[1])
    return total
"""
def cakeCalculatorDynamic(capacity, cakes):
    maxPossible = [0]*(capacity+1)
    for i in range(0,capacity+1):
        for cake in cakes:
            if cake[0]==0 and cake[1]>0:
                return float('inf')
            if i-cake[0]>=0:    
                if maxPossible[i-cake[0]]+cake[1]>maxPossible[i]:
                    maxPossible[i]=maxPossible[i-cake[0]]+cake[1]
    print(maxPossible)
    return maxPossible[capacity]

print(cakeCalculatorDynamic(20, [(7, 160), (3, 90), (2, 15)]))