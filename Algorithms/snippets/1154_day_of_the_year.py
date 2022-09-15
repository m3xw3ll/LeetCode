def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def day_of_year(date):
    date = date.split('-')
    days_dict = {
        0: 31,
        1: 28,
        2: 31,
        3: 30,
        4: 31,
        5: 30,
        6: 31,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31
    }

    if is_leap(int(date[0])):
        days_dict[1] = 29
    out = 0
    for i in range(0, int(date[1])-1):
        out += days_dict[i]

    return out + int(date[2])


print(day_of_year('2019-02-10'))
