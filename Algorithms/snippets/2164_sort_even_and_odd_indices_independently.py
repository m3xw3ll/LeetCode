def sort_even_odd(nums):
    if len(nums) == 2:
        return nums
    else:
        evens = list()
        odds = list()
        for i in range(len(nums)):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])

        evens.sort()
        odds.sort(reverse=True)

        evenidx = 0
        oddidx = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = evens[evenidx]
                evenidx += 1
            else:
                nums[i] = odds[oddidx]
                oddidx += 1
    return nums


print(sort_even_odd([4,1,2,3]))