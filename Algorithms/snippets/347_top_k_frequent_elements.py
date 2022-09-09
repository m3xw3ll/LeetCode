from collections import Counter


def top_k_frequent(nums, k):
    nums = Counter(nums)
    freq = dict(nums.most_common(k))
    return list(freq.keys())


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))