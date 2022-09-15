def count_odds(low, high):
    if low % 2 == 0:
        return (high - low + 1) // 2
    return ((high - low) // 2) + 1


print(count_odds(3, 7))