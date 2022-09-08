import datetime


def day_of_the_week(day, month, year):
    d = datetime.datetime(year, month, day)
    return d.strftime('%A')


print(day_of_the_week(31, 8, 2019))