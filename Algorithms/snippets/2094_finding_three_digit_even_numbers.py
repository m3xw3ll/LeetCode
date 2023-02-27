from collections import Counter


def find_even_numbers(digits):
    out = []
    c = Counter(digits)
    for i in range(100, 999, 2):
        if not Counter(int(d) for d in str(i)) - c:
            out.append(i)
    return out


print(find_even_numbers([2, 1, 3, 0]))