def prefix_count(words, pref):
    cnt = 0
    pref_len = len(pref)
    for word in words:
        if len(word) >= len(pref):
            if word[0:pref_len] == pref:
                cnt += 1
    return cnt


print(prefix_count(["leetcode", "win", "loops", "success"], "code"))
