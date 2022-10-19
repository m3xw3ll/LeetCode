def largest_integer(num):
    evens = list()
    odds = list()
    out = 0
    a = [int(x) for x in str(num)]

    for i in a:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    evens = sorted(evens)
    odds = sorted(odds)

    for i in range(len(a)):
        if a[i] % 2 == 0:
            out = out * 10 + evens.pop()
        else:
            out = out * 10 + odds.pop()
    return out


print(largest_integer(1234))