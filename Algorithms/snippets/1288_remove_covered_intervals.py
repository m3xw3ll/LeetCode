def remove_covered_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
    out = 0
    end = 0
    for _, e in intervals:
        if e > end:
            out += 1
            end = e
    return out


print(remove_covered_intervals([[1, 4], [3, 6], [2, 8]]))
