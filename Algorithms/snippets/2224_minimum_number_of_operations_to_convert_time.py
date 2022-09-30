def convert_time(current, correct):
    current_hour, current_min = current.split(':')
    correct_hour, correct_min = correct.split(':')
    current_time = (60 * int(current_hour)) + int(current_min)
    correct_time = (60 * int(correct_hour)) + int(correct_min)
    dif = abs(current_time - correct_time)
    cnt = 0
    for i in [60, 15, 5, 1]:
        cnt += dif // i
        dif %= i
    return cnt


print(convert_time('02:30', '04:35'))