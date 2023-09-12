def is_acronym(words, s):
    w = [word[0] for word in words]
    return ''.join(w) == s


print(is_acronym(words = ["alice","bob","charlie"], s = "abc"))