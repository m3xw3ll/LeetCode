def arrange_words(text):
    dict = {}
    out = ''
    words = text.split()
    for word in words:
        n = len(word)
        if n in dict:
            tmp = dict[n]
            tmp += ' ' + word.lower()
            dict[n] = tmp
        else:
            dict[n] = word.lower()

    for i in sorted(dict):
        out += dict[i] + ' '
    return out[:len(out) - 1].capitalize()


print(arrange_words(text="Keep calm and code on"))
