def create_target_array(nums, index):
    out = [] * len(nums)
    for i in range(len(nums)):
        out.insert(index[i], nums[i])
    return out


print(create_target_array([0,1,2,3,4], [0,1,2,2,1]))