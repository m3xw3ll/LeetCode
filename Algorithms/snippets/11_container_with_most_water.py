def max_area(height):
    m = 0
    i = 0
    j = len(height) - 1

    while i < j:
        width = abs(i - j)
        area = width * min(height[i], height[j])
        m = max(m, area)
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return m


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
