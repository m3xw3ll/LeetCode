def num_pairs_divisible_by_60(time):
    arr = [0] * 60
    out = 0
    for t in time:
        out += arr[-t % 60]
        arr[t % 60] += 1
    return out


print(num_pairs_divisible_by_60([30, 20, 150, 100, 40]))
