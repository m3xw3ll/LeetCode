def num_of_burgers(tomato_slices, cheese_slices):
    tx = tomato_slices - 2 * cheese_slices
    x = tx // 2
    y = cheese_slices - x
    return [x, y] if tx >= 0 and not tx % 2 and y >= 0 else []


print(num_of_burgers())