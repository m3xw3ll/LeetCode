def generate_the_string(n):
    out = 'a' * n
    if n % 2 == 0:
        return out[0:n-1] + 'b'
    return out


print(generate_the_string(4))
