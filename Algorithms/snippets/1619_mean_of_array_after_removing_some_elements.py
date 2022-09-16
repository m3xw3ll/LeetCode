def trim_mean(arr):
    arr = sorted(arr)
    perc = int(0.05 * len(arr))
    arr = arr[perc:]
    arr = arr[:-perc]

    return sum(arr) / len(arr)


print(trim_mean([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))
