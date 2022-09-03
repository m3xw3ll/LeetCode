from collections import Counter

def find_special_integer(arr):
    c = Counter(arr)
    hit = int(0.25 * len(arr))
    for val, cnt in c.items():
        if cnt > hit:
            return val


print(find_special_integer([1, 2, 2, 6, 6, 6, 6, 7, 10]))
