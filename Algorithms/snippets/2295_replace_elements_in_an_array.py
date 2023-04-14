def array_change(nums, operations):
    dic = {k: v for v, k in enumerate(nums)}

    for old, new in operations:
        tmp = dic[old]
        nums[tmp] = new
        dic[new] = tmp
        del dic[old]
    return nums


print(array_change(nums=[1, 2, 4, 6], operations=[[1, 3], [4, 7], [6, 1]]))
