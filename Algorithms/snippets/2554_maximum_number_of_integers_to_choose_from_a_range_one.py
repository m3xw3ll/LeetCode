import heapq


def max_count(banned, n, maxsum):
    s = [i for i in range(1, n + 1)]
    not_banned = list(set(s) - set(banned))
    not_banned = [-1 * i for i in not_banned]
    heapq.heapify(not_banned)
    while abs(sum(not_banned)) > maxsum:
        heapq.heappop(not_banned)
    return len(not_banned)


print(max_count(banned=[1, 6, 5], n=5, maxsum=6))
