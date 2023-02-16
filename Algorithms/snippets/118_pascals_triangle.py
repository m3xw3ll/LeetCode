def generate(num_rows):
    tmp = 0
    out = list()

    while tmp <= num_rows:
        if tmp == 1:
            out.append([1])
        if tmp == 2:
            out.append([1, 1])
        if tmp > 2:
            tmp_row = out[-1]
            new_row = []
            new_row.append(1)
            for i in range(len(tmp_row) - 1):
                new_row.append(tmp_row[i] + tmp_row[i+1])
            new_row.append(1)
            out.append(new_row)
        tmp += 1
    return out


print(generate(5))