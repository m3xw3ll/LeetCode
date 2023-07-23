def split_words_by_separator(words, separator):
    out = []
    for w in words:
        out += w.split(separator)
    return list(filter(None, out))


print(split_words_by_separator(words = ["$easy$","$problem$"], separator = "$"))
