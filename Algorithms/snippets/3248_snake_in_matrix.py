def final_position_of_snake(n, commands):
    matrix = [[i + j * n for i in range(n)] for j in range(n)]
    x = 0
    y = 0

    for d in commands:
        if d == "UP":
            y -= 1
        elif d == "DOWN":
            y += 1
        elif d == "RIGHT":
            x += 1
        else:
            x -= 1

    return matrix[y][x]


print(final_position_of_snake(n=2, commands=["RIGHT", "DOWN"]))
