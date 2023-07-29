def generate_matrix(n):
    left = 0
    right = n
    top = 0
    bottom = n
    out = [[0 for _ in range(n)] for _ in range(n)]
    val = 1
    while left < right and top < bottom:
        for i in range(left, right):
            out[top][i] = val
            val += 1
        top += 1

        for i in range(top, bottom):
            out[i][right - 1] = val
            val += 1
        right -= 1

        if not (left < right and top < bottom):
            break

        for i in range(right - 1, left - 1, -1):
            out[bottom - 1][i] = val
            val += 1
        bottom -= 1

        for i in range(bottom - 1, top - 1, -1):
            out[i][left] = val
            val += 1
        left += 1
    return out


print(generate_matrix(3))