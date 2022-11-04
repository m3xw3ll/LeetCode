def total_money(n):
    m = 0
    mondays = n // 7 + 1
    rem = n % 7
    for i in range(1, mondays):
        m += sum([i for i in range(i, i+7)])
    for j in range(mondays, mondays + rem):
        m += j
    return m


print(total_money(4))