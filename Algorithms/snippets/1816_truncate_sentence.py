def truncate_sentence(s, k):
    words = s.split(' ')
    return ' '.join(words[0:k])


print(truncate_sentence("Hello how are you Contestant", 4))