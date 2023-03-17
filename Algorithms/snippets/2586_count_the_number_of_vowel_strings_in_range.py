def vowel_strings(words, left, right):
    cnt = 0
    vows = set('aeiou')
    for i in range(left, right + 1):
        if words[i][0] in vows and words[i][-1] in vows:
            cnt += 1
    return cnt


print(vowel_strings(words=["are", "amy", "u"], left=0, right=2))
