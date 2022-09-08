import datetime


def days_between_dates(date1, date2):
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')

    return abs((date2 - date1).days)


print(days_between_dates('2019-06-29', '2019-06-30'))