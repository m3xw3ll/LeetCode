def sort_vowels(s):
    s = list(s)
    vows = []
    positions = []

    for idx, char in enumerate(s):
        if char in set('AEIOUaeiou'):
            vows.append(char)
            positions.append(idx)
    vows.sort()
    for char, pos in zip(vows, positions):
        s[pos] = char
    return ''.join(s)


print(sort_vowels('lEetcOde'))