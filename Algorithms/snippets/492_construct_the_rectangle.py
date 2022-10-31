def construct_rectangle(area):
    for l in range(int(area ** 0.5), 0, -1):
        if area % l == 0:
            return [area // l, l]


print(construct_rectangle(122122))