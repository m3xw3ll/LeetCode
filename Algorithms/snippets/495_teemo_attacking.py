def find_poisoned_duration(timeseries, duration):
    out = 0
    for i in range(len(timeseries) - 1):
        out += min(timeseries[i+1] - timeseries[i], duration)
    return out + duration


print(find_poisoned_duration(timeseries = [1,4], duration = 2))