def most_words_found(sentences):
    counts = []
    for s in sentences:
        l = len(s.split(' '))
        counts.append(l)
    return max(counts)


print(most_words_found(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))