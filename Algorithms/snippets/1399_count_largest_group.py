def count_largest_group(n):
    def sum_digits(num):
        return sum([int(d) for d in str(num)])
    dic = {}

    for i in range(1, n + 1):
        s = sum_digits(i)

        if s in dic:
            dic[s] += [s]
        else:
            dic[s] = [s]

    length = [len(value) for value in dic.values()]
    return length.count(max(length))


print(count_largest_group(13))