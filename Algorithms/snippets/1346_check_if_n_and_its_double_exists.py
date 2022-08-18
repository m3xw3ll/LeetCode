def check_if_exists(arr):
    tmp = set()
    for a in arr:
        if a * 2 in tmp or a / 2 in tmp:
            return True
        else:
            tmp.add(a)
    return False


print(check_if_exists([3, 1, 7, 11]))
