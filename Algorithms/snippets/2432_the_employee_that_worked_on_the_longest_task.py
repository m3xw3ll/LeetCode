def hardest_worker(n, logs):
    prev = 0
    ans = (0, 0)
    for id, time in logs:
        ans = min(ans, (prev - time, id))
        prev = time
    return ans[1]


print(hardest_worker(n=10, logs=[[0, 3], [2, 5], [0, 9], [1, 15]]))
