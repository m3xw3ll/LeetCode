def single_number(nums):
    dic = {}

    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    for k, v in dic.items():
        if v == 1:
            return k


print(single_number([2, 2, 3, 2]))
