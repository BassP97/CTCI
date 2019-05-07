#implement an algorithm to determine if a string has all unique characters

#inefficient version - n^2 runtime - pretty bad!
def isUniqueInefficient(toProcess):
    for i in range(0,len(toProcess)):
        for j in toProcess[i+1:len(toProcess)]:
            if toProcess[i] == j:
                return False
    return True

#Efficient version - using a dictionary we can get this down to n time!
def isUniqueEfficient(toProcess):
    letterDict = {}
    for i in toProcess:
        if i in letterDict:
            return False
        else:
            letterDict[i] = True
    return True

def main():
    toProcess = input("put in a word to check for unique characters: ")
    print(isUniqueEfficient(toProcess))
    print(isUniqueInefficient(toProcess))

main()
