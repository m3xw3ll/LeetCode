def top_k_frequent(words, k):
    dic = dict()
    for word in words:
        dic[word] = dic.get(word, 0) + 1
    return sorted(dic, key=lambda x: (-dic[x], x))[:k]


print(top_k_frequent(["i","love","leetcode","i","love","coding"], 2))