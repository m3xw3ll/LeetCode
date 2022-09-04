def num_jewels_is_stones(jewels, stones):
    cnt = 0
    for j in jewels:
        cnt += stones.count(j)
    return cnt


print(num_jewels_is_stones('aA', 'aAAbbbb'))