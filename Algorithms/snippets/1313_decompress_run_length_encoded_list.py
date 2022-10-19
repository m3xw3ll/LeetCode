def decompress_rle_list(nums):
    out = list()
    for i in range(0, len(nums), 2):
        out.extend([nums[i+1]] * nums[i])
    return out


print(decompress_rle_list([1, 2, 3, 4]))