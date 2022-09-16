def is_bad_version(n):
    versions = [False, False, False, False, True, True]
    return versions[n]


def first_bad_version(n):
    left = 0
    right = n
    while left < right:
        middle = (left + right) // 2
        if is_bad_version(middle):
            right = middle
        else:
            left = middle + 1
    return left


print(first_bad_version(5))
