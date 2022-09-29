def to_goat_latin(sentence):
    tokens = sentence.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    a_cnt = 1
    for token in range(len(tokens)):
        if tokens[token][0].lower() in vowels:
            tokens[token] = tokens[token] + 'ma'
        if tokens[token][0].lower() not in vowels:
            tokens[token] = tokens[token][1:] + tokens[token][0] + 'ma'
        tokens[token] = tokens[token] + 'a' * a_cnt
        a_cnt += 1
    return ' '.join(tokens)


print(to_goat_latin('I speak Goat Latin'))
