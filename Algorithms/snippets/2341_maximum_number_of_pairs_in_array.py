def number_of_pairs(nums):
    pairs = 0
    rem = 0
    dic = dict()
    for n in nums:
        dic[n] = dic.get(n, 0) + 1
    for v, k in dic.items():
        pairs += k // 2
        rem += k % 2
    return [pairs, rem]


print(number_of_pairs([1, 3, 2, 1, 3, 2, 2]))
