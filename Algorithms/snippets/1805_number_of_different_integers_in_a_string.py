def num_different_integers(word):
    out = []
    for char in word:
        if char.isalpha():
            out.append(' ')
        else:
            out.append(char)

    out = ''.join(out).split(' ')
    out = [int(char) for char in out if char]
    return len(set(out))


print(num_different_integers('a123bc34d8ef34'))