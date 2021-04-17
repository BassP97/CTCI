def containsDup(nums):
    seenBefore = set()
    for num in nums:
        if num in seenBefore:
            return True
        seenBefore.add(num)
    return False
