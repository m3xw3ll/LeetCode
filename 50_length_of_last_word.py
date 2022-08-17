def length_of_last_word(s):
    return len(s.strip()[::-1].split(' ')[0])


print(length_of_last_word("   fly me   to   the moon  "))
