def is_path_crossing(path):
    seen = set()
    seen.add((0, 0))
    x = 0
    y = 0
    for i in path:
        if i == 'N':
            y += 1
        elif i == 'S':
            y -= 1
        elif i == 'W':
            x += 1
        elif i == 'E':
            x -= 1
        if (x, y) in seen:
            return True
        seen.add((x, y))
    return False


print(is_path_crossing('NES'))
