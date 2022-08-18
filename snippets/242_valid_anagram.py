def is_anagram(s, t):
    s = sorted(s)
    t = sorted(t)
    return True if s == t else False

print(is_anagram('car', 'rat'))