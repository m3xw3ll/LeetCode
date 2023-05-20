from itertools import permutations


def largest_time_from_digits(arr):
    out = []

    for a, b, c, d in permutations(arr, 4):
        hour = 10 * a + b
        minute = 10 * c + d
        if hour < 24 and minute < 60:
            out.append((hour, minute))

    if not out: return ''
    l_time = max(out)
    return f'{str(l_time[0]).zfill(2)}:{str(l_time[1]).zfill(2)}'


print(largest_time_from_digits([1, 2, 3, 4]))
