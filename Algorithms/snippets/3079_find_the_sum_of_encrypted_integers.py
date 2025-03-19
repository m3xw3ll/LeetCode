def sum_of_encrypted_int(nums):
    return sum(int(str(max(int(x) for x in str(num))) * len(str(num))) for num in nums)


print(sum_of_encrypted_int([10, 21, 31]))
