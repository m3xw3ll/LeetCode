def combination_sum(candidates, target):
    out = []
    n = len(candidates)

    def bt(i, s, curr):
        if i >= n:
            if s == target:
                out.append(curr)
            return
        bt(i + 1, s, curr)
        if s + candidates[i] <= target:
            bt(i, s + candidates[i], curr + [candidates[i]])

    bt(0, 0, [])
    return out


print(combination_sum(candidates=[2, 3, 6, 7], target=7))
