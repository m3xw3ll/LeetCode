def dest_city(paths):
    start = [s[0] for s in paths]
    end = [e[1] for e in paths]
    return (set(end) - set(start)).pop()


print(dest_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
