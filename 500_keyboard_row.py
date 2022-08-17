def find_words(words):
    first = set('qwertyuiop')
    second = set('asdfghjkl')
    third = set('zxcvbnm')

    return [word for word in words if
            set(word.lower()).issubset(first) or
            set(word.lower()).issubset(second) or
            set(word.lower()).issubset(third)]


print(find_words(['Hello', 'Alaska', 'Dad', 'Peace']))