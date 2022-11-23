def find_judge(n, trust):
    trusted = [0] * (n + 1)
    for a, b in trust:
        trusted[a] -= 1
        trusted[b] += 1

    for i in range(1, len(trusted)):
        if trusted[i] == n-1:
            return i
    return -1


print(find_judge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
