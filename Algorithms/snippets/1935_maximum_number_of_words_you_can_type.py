def can_be_typed_words(text, broken_letters):
    cnt = 0
    letters = set(broken_letters)
    for word in text.split():
        if letters.isdisjoint(set(word)):
            cnt += 1
    return cnt


print(can_be_typed_words('leet code', 'e'))
