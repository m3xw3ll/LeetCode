def is_isomorphic(s, t):
    dic = dict()
    for i in range(len(s)):
        if s[i] in dic and dic[s[i]] != t[i]:
            return False
        dic[s[i]] = t[i]
    sset = set(list(s))
    tset = set(list(t))
    if len(sset) != len(tset):
        return False
    return True


print(is_isomorphic(s='egg', t='add'))