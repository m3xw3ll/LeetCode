def k_length_apart(nums, k):
    dst = k
    for n in nums:
        if n == 0:
            dst += 1
        elif n == 1 and dst >= k:
            dst = 0
        else:
            return False
    return True


print(k_length_apart(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2))
