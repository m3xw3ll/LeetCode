def sum_even_after_queries(nums, queries):
    out = []
    ev_sum = sum(x for x in nums if x % 2 == 0)
    for i in range(len(queries)):
        idx = queries[i][1]
        val = queries[i][0]
        if nums[idx] % 2 == 0:
            ev_sum -= nums[idx]
        nums[idx] += val
        if nums[idx] % 2 == 0:
            ev_sum += nums[idx]
        out.append(ev_sum)
    return out


print(sum_even_after_queries(nums=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]]))
