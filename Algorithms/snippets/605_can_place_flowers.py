def can_place_flowers(flowerbed, n):
    flowerbed = [0] + flowerbed + [0]
    cnt = 0
    if n == 0:
        return True
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            cnt += 1
            if cnt == n:
                return True
    return False


print(can_place_flowers([0, 0, 1, 0, 0], 1))