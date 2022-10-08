def num_of_strings(patterns, word):
    cnt = 0
    for pattern in patterns:
        if pattern in word:
            cnt += 1
    return cnt


print(num_of_strings(["a", "abc", "bc", "d"], 'abc'))
