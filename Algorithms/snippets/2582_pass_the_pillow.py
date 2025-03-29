def pass_the_pillow(n, time):
    direction = 1
    stand = 1
    while time:
        time -= 1
        if direction == 1:
            stand += 1
            if stand == n:
                direction = -1
        else:
            stand -= 1
            if stand == 1:
                direction = 1
    return stand


print(pass_the_pillow(n=4, time=5))
