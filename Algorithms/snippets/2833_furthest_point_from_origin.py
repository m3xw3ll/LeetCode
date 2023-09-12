from collections import Counter


def furthest_distance_from_origin(moves):
    cnt = Counter(moves)
    return abs(cnt['L'] - cnt['R'] + cnt['_'])


print(furthest_distance_from_origin('L_RL__R'))