def get_lucky(s, k):
    n = [str(ord(c) - ord('a') + 1) for c in s]
    n = ''.join(n)
    for i in range(k):
        n = str(sum(map(int, n)))
    return n


print(get_lucky('leetcode', 2))