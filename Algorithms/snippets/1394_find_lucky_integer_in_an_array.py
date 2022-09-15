from collections import Counter


def find_lucky(arr):
    arr = Counter(arr)
    out = []
    for i, v in arr.items():
        if i == v:
            out.append(i)
    return max(out) if len(out) > 0 else -1


print(find_lucky([2, 2, 2, 3, 3]))
