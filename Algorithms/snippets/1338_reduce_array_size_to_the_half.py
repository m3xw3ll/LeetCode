from collections import Counter


def min_set_size(arr):
    half = len(arr) // 2
    c = Counter(arr).most_common()
    total_cnt = 0
    for i in range(len(arr)):
        total_cnt += c[i][1]
        if total_cnt >= half:
            return i + 1


print(min_set_size([1, 9]))
