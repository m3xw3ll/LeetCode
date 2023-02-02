def time_required_to_buy(tickets, k):
    i = 0
    secs = 0
    while tickets[k] != 0:
        if tickets[i] != 0:
            tickets[i] -= 1
            secs += 1
        i = (i + 1) % len(tickets)
    return secs


print(time_required_to_buy(tickets=[2, 3, 2], k=2))
