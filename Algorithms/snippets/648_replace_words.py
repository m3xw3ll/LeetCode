def replace_words(dictionary, sentence):
    words = sentence.split()
    dic = set(dictionary)
    out = list()

    for w in words:
        root = False
        for i in range(len(w)):
            if w[:i+1] in dic:
                root = True
                out.append(w[:i+1])
                break
        if not root:
            out.append(w)
    return ' '.join(out)


print(replace_words(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
