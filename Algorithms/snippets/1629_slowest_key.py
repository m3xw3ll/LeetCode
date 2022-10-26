def slowest_key(release_times, key_pressed):
    times = list()
    times.append([release_times[0], key_pressed[0]])
    for i in range(1, len(key_pressed)):
        times.append([release_times[i] - release_times[i - 1], key_pressed[i]])

    slowest = max(times)
    return slowest[1]


print(slowest_key(release_times=[9, 29, 49, 50], key_pressed="cbcd"))
