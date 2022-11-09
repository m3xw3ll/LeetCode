def three_sum(nums):
    pos = []
    neg = []
    zer = []
    out = set()

    for n in nums:
        if n < 0:
            neg.append(n)
        elif n > 0:
            pos.append(n)
        else:
            zer.append(n)

    pos_set = set(pos)
    neg_set = set(neg)

    if zer:
        for i in pos_set:
            if -1*i in neg_set:
                out.add((-i, 0, i))

    if len(zer) >= 3:
        out.add((0, 0, 0))

    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            t = -1 * (pos[i] + pos[j])
            if t in neg_set:
                out.add(tuple(sorted([pos[i], pos[j], t])))

    for i in range(len(neg)):
        for j in range(i+1, len(neg)):
            t = -1 * (neg[i] + neg[j])
            if t in pos_set:
                out.add(tuple(sorted([neg[i], neg[j], t])))

    return out


print(three_sum([-1,0,1,2,-1,-4]))