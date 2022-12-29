def buddy_strings(s, goal):
    if len(s) != len(goal) or sorted(s) != sorted(goal):
        return False

    cnt = 0
    rep = 0
    equals = set()
    for i, y in zip(s, goal):
        if i == y:
            if i in equals:
                rep += 1
            else:
                equals.add(i)
        else:
            cnt += 1
    return True if cnt == 2 or (cnt == 0 and rep) else False


print(buddy_strings('ab', 'ba'))