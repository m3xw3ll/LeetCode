def count_prefixes(words, s):
    cnt = 0
    for word in words:
        if s.startswith(word):
            cnt += 1
    return cnt


print(count_prefixes(["a","b","c","ab","bc","abc"], 'abc'))