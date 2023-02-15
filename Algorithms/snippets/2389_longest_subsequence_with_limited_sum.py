import bisect
from itertools import accumulate


def answer_queries(nums, queries):
    nums = list(accumulate(sorted(nums)))
    return [bisect.bisect_right(nums, q) for q in queries]


print(answer_queries(nums=[4, 5, 2, 1], queries=[3, 10, 21]))
