def string_matching(words):
    sorted_words = sorted(words, key=len)
    out = []

    for i in range(len(sorted_words)):
        for j in range(i+1, len(sorted_words)):
            if sorted_words[i] in sorted_words[j]:
                out.append(sorted_words[i])
                break
    return out


print(string_matching(["mass", "as", "hero", "superhero"]))
