from collections import Counter

def frequency_sort(s):
    s = Counter(s)
    ss = sorted(s, key=s.get, reverse=True)
    print(ss)
    print(s)
    out = ''
    for i in ss:
        for j in range(s[i]):
            out += i
    return out


print(frequency_sort('tree'))