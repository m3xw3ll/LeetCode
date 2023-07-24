from itertools import accumulate


def vowel_strings(words, queries):
    vowels = 'aeiou'
    counts = [0] * len(words)
    out = []
    for idx, word in enumerate(words):
        if word[0] in vowels and word[-1] in vowels:
            counts[idx] += 1

    acc = list(accumulate(counts, initial=0))
    print(acc)
    for left, right in queries:
        out.append(acc[right + 1] - acc[left])
    return out


print(vowel_strings(words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]))
