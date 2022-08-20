def is_ugly(n):
    primes = [2, 3, 5]
    if n == 0:
        return False
    for p in primes:
        while n % p == 0:
            n = n // p
    return n == 1


print(is_ugly(6))
