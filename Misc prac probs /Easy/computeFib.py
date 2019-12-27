import time
def computeFib(n):
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]

def computeFibRec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return computeFibRec(n-1)+computeFibRec(n-2)

start_time = time.time()
print(computeFib(38))
elapsed_time = time.time() - start_time
print(elapsed_time)


