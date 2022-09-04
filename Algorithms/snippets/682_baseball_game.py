def cal_points(ops):
    rec = []
    operation = ['C', 'D', '+']

    for value in ops:
        if value not in operation:
            rec.append(int(value))
        if value == 'C':
            rec.pop()
        if value == 'D':
            rec.append(rec[-1] * 2)
        if value == '+':
            rec.append(sum(rec[-2:]))

    return sum(rec)


print(cal_points(["1","C"]))