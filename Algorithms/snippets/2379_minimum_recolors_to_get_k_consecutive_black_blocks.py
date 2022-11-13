def minimum_recolors(blocks, k):
    out = k
    for i in range(0, len(blocks) - k + 1):
        out = min(out, k - blocks[i:i+k].count('B'))
    return out


print(minimum_recolors('WBBWWBBWBW', 7))