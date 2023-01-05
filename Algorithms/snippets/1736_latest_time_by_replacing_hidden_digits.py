def maximum_time(time):
    time = list(time)
    for idx, char in enumerate(time):
        if char == '?':
            if idx == 0:
                time[idx] = '2' if time[1] <= '3' or time[1] == '?' else '1'
            elif idx == 1:
                time[idx] = '3' if time[0] == '2' else '9'
            elif idx == 3:
                time[idx] = '5'
            elif idx == 4:
                time[idx] = '9'
    return ''.join(time)


print(maximum_time('2?:?0'))