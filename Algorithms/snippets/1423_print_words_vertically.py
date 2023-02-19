from itertools import zip_longest


def print_vertically(s):
    out = list()
    for x in zip_longest(*s.split(), fillvalue=' '):
        out.append(''.join(x))
    return [x.rstrip() for x in out]


print(print_vertically("TO BE OR NOT TO BE"))