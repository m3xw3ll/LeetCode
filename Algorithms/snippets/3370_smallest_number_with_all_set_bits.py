def smallest_number(n):
    if (n & (n + 1)) == 0:
        return n
    return smallest_number(n+1)


print(smallest_number(10))