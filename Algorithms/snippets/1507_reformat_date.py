def reformat_date(date):
    date = date.split()
    date[0] = date[0][:-2]
    date[0] = '0' + date[0] if len(date[0]) == 1 else date[0]
    months = {'Jan': '01',
              'Feb': '02',
              'Mar': '03',
              'Apr': '04',
              'May': '05',
              'Jun': '06',
              'Jul': '07',
              'Aug': '08',
              'Sep': '09',
              'Oct': '10',
              'Nov': '11',
              'Dec': '12',}
    return f'{date[2]}-{months[date[1]]}-{date[0]}'


print(reformat_date('22th Apr 2023'))
