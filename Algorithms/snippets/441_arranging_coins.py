def arrange_coins(n):
    i = 1
    stair = 0
    while i <= n:
        stair += 1
        n -= i
        i += 1
    return stair


print(arrange_coins(8))