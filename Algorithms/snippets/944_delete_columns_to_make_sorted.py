def min_deletion_size(strs):
    out = 0
    for col in zip(*strs):
        if sorted(col) != list(col):
            out += 1
    return out


print(min_deletion_size(["cba", "daf", "ghi"]))
