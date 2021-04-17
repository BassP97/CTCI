def prodArrExceptSelf(arr):
    res = [1 for i in range(len(arr))]
    currProd = arr[0]
    for i in range(1, len(arr)):
        res[i] = currProd
        currProd *= arr[i]
    print(res)
    currProd = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        print("before ", res[i])
        res[i] = res[i]*currProd
        currProd = currProd*arr[i]
        print("After ", res[i])
    return res


print(prodArrExceptSelf([1, 2, 3, 4]))
