def find_subarrays(nums):
    n = set()
    for i in range(len(nums) - 1):
        tmp = nums[i] + nums[i+1]
        if tmp in n:
            return True
        n.add(tmp)
    return False


print(find_subarrays([4, 2, 4]))