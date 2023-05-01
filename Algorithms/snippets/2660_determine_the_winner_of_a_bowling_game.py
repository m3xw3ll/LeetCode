def get_score(rounds):
    score = 0
    for i in range(len(rounds)):
        print(rounds[i-1])
        if 0 < i <= 1 and rounds[i-1] == 10:
            score += 2 * rounds[i]
        elif i > 1 and 10 in rounds[i-2:i]:
            score += 2 * rounds[i]
        else:
            score += rounds[i]
    return score


def is_winner(player1, player2):
    p1_score = get_score(player1)
    p2_score = get_score(player2)

    if p1_score == p2_score: return 0
    return 1 if p1_score > p2_score else 2


print(is_winner(player1=[5, 6, 1, 10], player2=[5, 1, 10, 5]))
