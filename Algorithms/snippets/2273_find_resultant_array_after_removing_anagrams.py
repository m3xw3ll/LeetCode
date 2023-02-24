def remove_anagrams(words):
    i = 0
    while True:
        if i >= len(words) - 1:
            break
        if sorted(words[i]) == sorted(words[i + 1]):
            words.pop(i+1)
            i -= 1
        i += 1
    return words


print(remove_anagrams(["abba", "baba", "bbaa", "cd", "cd"]))
