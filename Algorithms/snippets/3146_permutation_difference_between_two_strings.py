def find_permutation_difference(s, t):
    d = {}
    out = 0
    for i in range(len(t)):
        d[t[i]] = i

    for i in range(len(s)):
        out += abs(i - d[s[i]])
    return out



print(find_permutation_difference(s = "abc", t = "bac"))