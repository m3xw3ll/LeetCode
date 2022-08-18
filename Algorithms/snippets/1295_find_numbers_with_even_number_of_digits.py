def find_numbers(nums):
    cnt = 0
    nums = map(str, nums)
    for n in nums:
        if len(n) % 2 == 0:
            cnt += 1
    return cnt


print(find_numbers([555, 901, 482, 1771]))
