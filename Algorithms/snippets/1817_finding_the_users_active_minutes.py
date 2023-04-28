def finding_users_active_minutes(logs, k):
    out = [0] * k
    cnts = {}
    for i, t in logs:
        cnts.setdefault(i, set()).add(t)

    for v in cnts.values():
        if len(v) <= k:
            out[len(v) - 1] += 1
    return out


print(finding_users_active_minutes(logs=[[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], k=5))
