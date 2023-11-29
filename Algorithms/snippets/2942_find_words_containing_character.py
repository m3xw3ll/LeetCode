def find_words_containing(words, x):
    out = []
    for i in range(len(words)):
        if x in words[i]:
            out.append(i)
    return out


print(find_words_containing(words=["leet", "code"], x="e"))
