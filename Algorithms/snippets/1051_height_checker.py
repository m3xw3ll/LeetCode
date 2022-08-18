def height_checker(heights):
    sorted_heights = sorted(heights)
    cnt = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            cnt += 1
    return cnt


print(height_checker([5, 1, 2, 3, 4]))
