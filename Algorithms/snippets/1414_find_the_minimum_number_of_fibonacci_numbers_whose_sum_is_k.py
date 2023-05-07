def find_min_fibonacci_numbers(k):
    fib = [1, 1]
    l = 2
    while fib[-1] + fib[-2] <= k:
        fib.append(fib[-1] + fib[-2])
        l += 1
    count = 0
    while l and k:
        if fib[l - 1] > k:
            l -= 1
        else:
            k -= fib[l - 1]
            count += 1
    return count


print(find_min_fibonacci_numbers(7))