def max_repeating(sequence, word):
    cnt = 0
    i = 1
    while word * i in sequence:
        cnt += 1
        i += 1
    return cnt


print(max_repeating(sequence="ababc", word="ba"))
