def array_rank_transform(arr):
    s = 1
    dic = dict()
    for i in sorted(list(set(arr))):
        dic[i] = s
        s += 1
    return [dic[x] for x in arr]


print(array_rank_transform([40, 10, 20, 30]))
