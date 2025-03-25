def number_of_special_chars(word):
    characters = list(map(chr, range(97, 123)))
    cnt = 0
    for char in characters:
        if char in word and char.upper() in word:
            cnt += 1
    return cnt


print(number_of_special_chars("aaAbcBC"))