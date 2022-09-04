from collections import Counter, defaultdict

def frequency_sort(nums):
    out = []
    cnt = Counter(nums)
    freqdict = defaultdict(list)
    for k, v in cnt.items():
        freqdict[v].append(k)
    for f in sorted(freqdict):
        for num in sorted(freqdict[f], reverse=True):
            out = out + [num] * f
    return out


print(frequency_sort([1, 1, 2, 2, 2, 3]))