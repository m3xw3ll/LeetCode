def distribute_candies(n, limit):
    cnt = 0
    for i in range(limit +1 ):
        for j in range(limit + 1):
            for k in range(limit + 1):
                if i + j + k == n:
                    cnt += 1
    return cnt


print(distribute_candies(n=5, limit=2))