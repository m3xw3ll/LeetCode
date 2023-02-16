def get_row(row_index):
    if row_index == 0:
        return [1]

    prev = get_row(row_index - 1)
    cur_row = [1]
    for i in range(len(prev) - 1):
        cur_row.append(prev[i] + prev[i+1])
    cur_row.append(1)
    return cur_row


print(get_row(3))