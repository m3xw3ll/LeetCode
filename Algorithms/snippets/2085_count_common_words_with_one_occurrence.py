from collections import Counter


def count_words(words1, words2):
    words1 = Counter(words1)
    words2 = Counter(words2)
    cnt = 0
    for word in words1:
        if words1[word] == 1 and words2[word] == 1:
            cnt += 1
    return cnt


print(count_words(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]))