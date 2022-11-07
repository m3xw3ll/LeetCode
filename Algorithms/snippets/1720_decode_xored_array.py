def decode(encoded, first):
    out = [0] * (len(encoded) + 1)
    out[0] = first
    for i in range(len(encoded)):
        out[i+1] = encoded[i] ^ out[i]
    return out


print(decode(encoded=[1, 2, 3], first=1))
