def sort_string(s):
    out = ''
    s = list(s)
    while s:
        for letter in sorted(set(s)):
            s.remove(letter)
            out += letter
        for letter in sorted(set(s), reverse=True):
            s.remove(letter)
            out += letter
    return out


print(sort_string('aaaabbbbcccc'))