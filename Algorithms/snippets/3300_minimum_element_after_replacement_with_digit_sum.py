def min_element(nums):
    m = float('inf')
    for n in nums:
        digs_sum = sum(int(x) for x in str(n))
        m = min(m, digs_sum)
    return m


print(min_element([10,12,13,14]))