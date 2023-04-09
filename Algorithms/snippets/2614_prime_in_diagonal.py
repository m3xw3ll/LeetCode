def diagonal_prime(nums):
    def is_prime(val):
        if val == 1:
            return False
        i = 2
        while i * i <= val:
            if val % i == 0:
                return False
            i += 1
        return True

    vals = set()
    out = 0
    for i in range(0, len(nums)):
        vals.add((nums[i][i]))
    for i in range(0, len(nums)):
        vals.add((nums[i][~i]))

    for v in list(vals):
        if is_prime(v):
            out = max(out, v)
    return out


print(diagonal_prime([[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
