def most_frequent_even(nums):
    evens = list()
    dic = dict()
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
            dic[i] = dic.get(i, 0) + 1

    if len(evens) > 0:
        cancicates = sorted([key for m in [max(dic.values())] for key, val in dic.items() if val == m])
        return cancicates[0] if cancicates else -1
    return -1


print(most_frequent_even([29, 47, 21, 41, 13, 37, 25, 7]))
