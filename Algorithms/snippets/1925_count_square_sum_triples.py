import math


def count_triples(n):
    cnt = 0
    for i in range(1, n):
        for j in range(i+1, n):
            s = math.sqrt(i**2 + j**2)
            if int(s) == s and s <= n:
                cnt += 2
    return cnt


print(count_triples(18))