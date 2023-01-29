from collections import Counter


def merge_similar_items(items1, items2):
    items = items1 + items2
    c = Counter()
    for value, weight in items:
        c[value] += weight

    return sorted(c.items())


print(merge_similar_items(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]))
