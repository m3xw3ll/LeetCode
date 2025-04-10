def count_prefix_suffix_pairs(words):
    cnt = 0
    for a in range(len(words)):
        for b in range(a + 1, len(words)):
            if words[b].startswith(words[a]) and words[b].endswith(words[a]):
                cnt += 1
    return cnt


print(count_prefix_suffix_pairs(words = ["a","aba","ababa","aa"]))