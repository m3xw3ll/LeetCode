def num_rescue_boats(people, limit):
    cnt = 0
    people = sorted(people)
    lightest = 0
    heaviest = len(people) -1

    while lightest <= heaviest:
        if people[lightest] + people[heaviest] <= limit:
            lightest += 1
        cnt += 1
        heaviest -= 1

    return cnt


print(num_rescue_boats([3, 5, 3, 4], 5))