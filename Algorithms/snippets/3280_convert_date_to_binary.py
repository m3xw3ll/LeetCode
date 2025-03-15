def convert_date_to_binary(date):
    year, month, day = map(int, date.split('-'))
    return '-'.join([bin(year)[2:], bin(month)[2:], bin(day)[2:]])


print(convert_date_to_binary("2080-02-29"))