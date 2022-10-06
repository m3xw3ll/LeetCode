def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start = max(arrive_alice, arrive_bob)
    sm, sd = map(int, start.split("-"))
    end = min(leave_alice, leave_bob)
    em, ed = map(int, end.split("-"))
    res = 0
    for m in range(sm + 1, em):
        res += days[m - 1]
    if em > sm:
        res += days[sm - 1] - sd + ed + 1
    elif em == sm:
        res += max(ed - sd + 1, 0)
    return res

print(count_days_together(arrive_alice = "08-15", leave_alice = "08-18", arrive_bob = "08-16", leave_bob = "08-19"))