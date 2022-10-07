def count_negatives(grid):
    return sum(binary_search(row) for row in grid)


def binary_search(row):
    left = 0
    right = len(row) - 1

    while left <= right:
        middle = (left + right) // 2
        if row[middle] < 0:
            right = middle - 1
        else:
            left = middle + 1
    return len(row) - left


print(count_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
