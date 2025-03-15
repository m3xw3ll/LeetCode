def score_of_string(s):
    score = 0
    asci_numbers = [ord(i) for i in s]
    for i in range(len(asci_numbers) - 1):
        score += abs(asci_numbers[i] - asci_numbers[i+1])
    return score


print(score_of_string("hello"))