def make_equal(words):
    chars = ''.join(words)
    dist_chars = set(chars)

    for char in dist_chars:
        if chars.count(char) % len(words) != 0:
            return False
    return True


print(make_equal(words=["abc", "aabc", "bc"]))
