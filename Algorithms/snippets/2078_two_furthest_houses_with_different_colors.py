def max_distance(colors):
    dist = 0
    l = len(colors)
    for i in range(l):
        for j in range(l):
            if colors[i] != colors[j]:
                dist = max(dist, abs(i - j))
    return dist


print(max_distance([1, 1, 1, 6, 1, 1, 1]))
