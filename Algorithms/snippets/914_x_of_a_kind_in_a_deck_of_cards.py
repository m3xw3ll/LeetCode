from collections import Counter
from functools import reduce
import math


def has_groups_size_x(deck):
    c = Counter(deck)
    x = reduce(math.gcd, list(c.values()))
    return x > 1


print(has_groups_size_x([1, 2, 3, 4, 4, 3, 2, 1]))
