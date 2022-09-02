def halves_are_alike(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    asum = 0
    bsum = 0
    a = s[0:len(s) // 2]
    b = s[len(s) // 2:]

    for char in a:
        if char in vowels:
            asum += 1
    for char in b:
        if char in vowels:
            bsum += 1

    return True if asum == bsum else False


print(halves_are_alike('book'))