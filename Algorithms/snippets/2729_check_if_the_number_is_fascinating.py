def is_fascinating(n):
    out = [*(str(n) + str(n * 2) + str(n * 3))]
    return True if len(out) == 9 and '0' and len(out) == len(set(out)) not in out else False


print(is_fascinating(192))