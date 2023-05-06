def match_players_and_trainers(players, trainers):
    cnt = 0
    players = sorted(players)
    trainers = sorted(trainers)
    p, t = 0, 0

    while p < len(players) and t < len(trainers):
        if players[p] <= trainers[t]:
            cnt += 1
            p += 1
        t += 1
    return cnt


print(match_players_and_trainers(players=[4, 7, 9], trainers=[8, 2, 5, 8]))
