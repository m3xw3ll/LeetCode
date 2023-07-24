def sieve_of_eratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    return prime


def find_prime_pairs(n):
    out = []
    primes = sieve_of_eratosthenes(n)
    for i in range(2, n // 2 + 1):
        if primes[i] and primes[n - i]:
            out.append([i, n - i])
    return out


print(find_prime_pairs(10))