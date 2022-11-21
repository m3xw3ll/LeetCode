def count_vowel_substrings(word):
    cnt = 0
    vowels = set('aeiou')

    for i in range(len(word)):
        tmp = set()
        for j in range(i, len(word)):
            if word[j] in vowels:
                tmp.add(word[j])
                if len(tmp) == 5:
                    cnt += 1
            else:
                break
    return cnt


print(count_vowel_substrings('unicornarihan'))