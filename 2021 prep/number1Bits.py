def number1Bits(num):
    numBits = 0
    while num > 0:
        if num & 1:
            num = num ^ 1
            numBits += 1
        num = num >> 1
    return numBits


print(number1Bits(7))
print(number1Bits(8))
print(number1Bits(15))
