def check_arithmetic_subarrays(nums, l, r):
    runs = len(l)
    out = [False] * runs
    for i in range(runs):
        tmp = nums[l[i]:r[i]+1]
        tmp.sort()
        differences = [tmp[i+1] - tmp[i] for i in range(len(tmp)-1)]
        if all(difference == differences[0] for difference in differences):
            out[i] = True
    return out


print(check_arithmetic_subarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))
