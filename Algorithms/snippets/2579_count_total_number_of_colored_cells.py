def colored_cells(n):
    out = 1
    for i in range(1, n):
        out += i * 4
    return out


print(colored_cells(3))