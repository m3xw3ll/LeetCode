def sort_array_by_parity_2(nums):
    out = [0] * len(nums)
    evens = list()
    odds = list()

    for n in nums:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)

    for i in range(len(out)):
        if i % 2 == 0:
            out[i] = evens.pop()
        else:
            out[i] = odds.pop()
    return out


print(sort_array_by_parity_2([4, 2, 5, 7]))