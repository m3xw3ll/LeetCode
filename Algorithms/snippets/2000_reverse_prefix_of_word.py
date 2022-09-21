def reverse_prefix(word, ch):
    if ch not in word:
        return word

    idx = word.index(ch)
    return word[0:idx+1][::-1] + word[idx+1:]


print(reverse_prefix('abcdefd', 'd'))
