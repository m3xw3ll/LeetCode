from collections import Counter


def can_be_equal(target, arr):
    if len(arr) > len(target):
        return False
    t = Counter(target)
    a = Counter(arr)

    for k, v in a.items():
        if k in t and v == t[k]:
            continue
        else:
            return False
    return True


print(can_be_equal(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
