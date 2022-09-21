def find_center(edges):
    out = [0] * (len(edges) + 2)

    for edge in edges:
        out[edge[0]] += 1
        out[edge[1]] += 1

    return out.index(max(out))


print(find_center([[1, 2], [2, 3], [4, 2]]))
