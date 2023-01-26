def find_lus_length(a, b):
    if a == b:
        return -1
    return max(len(a), len(b))


print(find_lus_length(a="aba", b="cdc"))
