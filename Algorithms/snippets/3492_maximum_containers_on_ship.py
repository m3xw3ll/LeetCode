def max_containers(n, w, max_weight):
    return min(n*n, max_weight // w)


print(max_containers(n = 2, w = 3, max_weight = 15))