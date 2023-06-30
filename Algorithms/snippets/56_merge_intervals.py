def merge(intervals):
    intervals = sorted(intervals, key=lambda i: i[0])
    out = [intervals[0]]
    for start, end in intervals[1:]:
        if out[-1][1] >= start:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([start, end])
    return out


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
