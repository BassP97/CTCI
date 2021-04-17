def threeSum(arr):
    arr.sort()
    seen = set()
    res = []
    for i in range(len(arr)-2):
        l = i+1
        r = len(arr)-1
        while l < r:
            s = arr[i]+arr[l]+arr[r]
            if s == 0 and frozenset([arr[i], arr[l], arr[r]]) not in seen:
                print(arr[i])
                print(arr[l])
                print(arr[r])
                res.append([arr[i], arr[l], arr[r]])
                seen.add(frozenset([arr[i], arr[l], arr[r]]))
            if s >= 0:
                r -= 1
            if s <= 0:
                l += 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
