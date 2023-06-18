def distance_traveled(main_tank, additional_tank):
    out = 0
    tmp = 0
    while main_tank > 0:
        out += 10
        tmp += 1
        main_tank -= 1
        if additional_tank > 0 and tmp % 5 == 0:
            main_tank += 1
            additional_tank -= 1
    return out


print(distance_traveled(main_tank = 5, additional_tank = 10))