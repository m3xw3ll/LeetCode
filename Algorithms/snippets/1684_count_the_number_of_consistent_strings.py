def count_consistent_strings(allowed, words):
    allowed = [*allowed]
    cnt = 0
    for word in words:
        if set(word).issubset(allowed):
            cnt += 1
    return cnt


print(count_consistent_strings('ab', ["ad","bd","aaab","baa","badab"]))