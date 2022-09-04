from collections import Counter

def count_characters(words, chars):
    cnt = 0
    chars = Counter(chars)
    for word in words:
        tmp = Counter(word)
        k = 0
        for c in word:
            if chars[c] < tmp[c]:
                k = 1
                continue
        if k == 0:
            cnt += len(word)
    return cnt



print(count_characters(["cat","bt","hat","tree"], 'atach'))