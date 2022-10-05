def length_of_longest_substring(s):
    word = ''
    out = 0

    for i in range(len(s)):
        if s[i] in word:
            out = max(len(word), out)
            idx = word.index(s[i])
            word = word[idx+1:]
        word += s[i]
    return max(len(word), out)


print(length_of_longest_substring('abcabcbb'))