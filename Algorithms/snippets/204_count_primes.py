def count_primes(n):
    seen = [0] * n
    out = 0
    for num in range(2, n):
        if seen[num]:
            continue
        out += 1
        seen[num*num:n:num] = [1] * ((n - 1) // num - num +1)
    return out


print(count_primes(3))
