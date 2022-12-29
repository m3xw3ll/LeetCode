def similar_pairs(words):
    cnt = 0
    for i, w1 in enumerate(words):
        for w2 in words[i + 1:]:
            cnt += set(w1) == set(w2)
    return cnt


print(similar_pairs(["aba", "aabb", "abcd", "bac", "aabc"]))
