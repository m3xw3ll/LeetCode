def kids_with_candies(candies, extra_candies):
    out = []
    maxcand = max(candies)

    for c in candies:
        if maxcand > c + extra_candies:
            out.append(False)
        else:
            out.append(True)
    return out


print(kids_with_candies([12, 1, 12], 10))