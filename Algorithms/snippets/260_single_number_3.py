def single_number(nums):
    dic = {}
    out = []

    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    for k, v in dic.items():
        if v == 1:
            out.append(k)
    return out


print(single_number([1, 2, 1, 3, 2, 5]))
