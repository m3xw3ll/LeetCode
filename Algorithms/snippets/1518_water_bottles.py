def num_water_bottles(num_bottles, num_exchange):
    out = num_bottles
    while num_bottles >= num_exchange:
        tmp = num_bottles // num_exchange
        num_bottles = num_bottles % num_exchange + tmp
        out += tmp
    return out


print(num_water_bottles(15, 4))