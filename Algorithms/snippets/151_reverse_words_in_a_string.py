def reverse_words(s):
    s = s.split()
    return ' '.join(s[::-1])


print(reverse_words("  hello world  "))