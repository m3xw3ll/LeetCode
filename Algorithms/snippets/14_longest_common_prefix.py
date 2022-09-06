def longest_common_prefix(strs):
    out = ''
    shortest = min(strs, key=len)
    for i in range(len(shortest)):
        p = all([x[i] == shortest[i] for x in strs])
        if p:
            out += shortest[i]
        else:
            break
    return out


print(longest_common_prefix(['dog', 'racecar', 'car']))