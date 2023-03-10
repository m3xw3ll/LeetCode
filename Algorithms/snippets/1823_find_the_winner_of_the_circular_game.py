def find_the_winner(n, k):
    l = [i for i in range(1, n+1)]
    k -= 1
    idx = k
    while len(l) > 1:
        l.pop(idx)
        idx = (idx + k) % len(l)
    return l[0]


print(find_the_winner(n=5, k=2))