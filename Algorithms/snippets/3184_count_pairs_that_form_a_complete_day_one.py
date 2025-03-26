def count_complete_day_pairs(hours):
    cnt = 0
    for i in range(len(hours)):
        for j in range(i + 1, len(hours)):
            if (hours[i] + hours[j]) % 24 == 0:
                cnt += 1
    return cnt


print(count_complete_day_pairs([12, 12, 30, 24, 24]))
