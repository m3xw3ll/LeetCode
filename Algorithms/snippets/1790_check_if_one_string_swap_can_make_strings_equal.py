def are_almost_equal(s1, s2):
    cnt = 0
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
        if cnt > 2:
            return False
    return True


print(are_almost_equal('bank', 'kanb'))
