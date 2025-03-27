def maximum_population(logs):
    d = {}

    for log in logs:
        birth, death = log
        for i in range(birth, death):
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    max_pop = max(d.values())
    return min(i for i in d if d[i] == max_pop)


print(maximum_population([[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]))
