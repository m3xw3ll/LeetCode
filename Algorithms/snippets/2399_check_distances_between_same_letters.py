def check_distances(s, distance):
    dic = {}
    l = 97
    for i in distance:
        dic[chr(l)] = i
        l += 1

    for i in set(s):
        first = s.index(i)
        last = s.rindex(i)

        diff = last - first - 1
        if dic[i] != diff:
            return False
    return True


print(check_distances(s="abaccb",
                      distance=[1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
