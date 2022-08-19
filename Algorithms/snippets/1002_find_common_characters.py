def common_chars(words):
    out = []
    d = {}
    for s in set(words[0]):
        d[s] = min([word.count(s) for word in words])
    for k, v in d.items():
        out += [k] * v
    return out


print(common_chars(["bella", "label", "roller"]))
