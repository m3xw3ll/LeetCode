def repeated_n_times(nums):
    dic = {}
    for n in nums:
        dic[n] = dic.get(n, 0) + 1

    for k, v in dic.items():
        if v == len(nums) // 2:
            return k


print(repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]))
