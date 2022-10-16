def largest_altitude(gain):
    altitudes = [0]
    for g in gain:
        altitudes.append(altitudes[-1] + g)
    return max(altitudes)


print(largest_altitude([-4, -3, -2, -1, 4, 3, 2]))
