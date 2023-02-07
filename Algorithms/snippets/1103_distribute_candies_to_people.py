def distribute_candies(candies, num_people):
    out = [0] * num_people
    i = 0
    j = 1
    while candies > 0:
        if i == len(out):
            i = 0
        if candies >= j:
            out[i] += j
            candies -= j
            j += 1
        else:
            out[i] += candies
            break
        i += 1
    return out


print(distribute_candies(candies=7, num_people=4))
