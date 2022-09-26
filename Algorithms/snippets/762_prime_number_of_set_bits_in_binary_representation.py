def prime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def count_prime_set_bits(left, right):
    cnt = 0
    for i in range(left, right+1):
        binary = format(i, 'b')
        if prime(binary.count('1')):
            cnt += 1
    return cnt


print(count_prime_set_bits(6, 10))