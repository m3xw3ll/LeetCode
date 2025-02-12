def count_partitions(nums):
    cnt = 0
    for i in range(len(nums) - 1):
        if (sum(nums[0:i+1]) - sum(nums[i+1:len(nums)])) % 2 == 0:
            cnt += 1
    return cnt


print(count_partitions([10,10,3,7,6]))