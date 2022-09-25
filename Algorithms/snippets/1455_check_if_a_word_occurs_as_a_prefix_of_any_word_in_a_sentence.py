def is_prefix_of_word(sentence, search_word):
    sentence = sentence.split()
    for idx, word in enumerate(sentence):
        if word.startswith(search_word):
            return idx + 1
    return -1


print(is_prefix_of_word('i love eating burger', 'burg'))
