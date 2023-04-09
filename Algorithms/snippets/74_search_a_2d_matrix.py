def search_matrix(matrix, target):
    flat_matrix = [item for sublist in matrix for item in sublist]
    left = 0
    right = len(flat_matrix) - 1

    while left <= right:
        middle = (left + right) // 2
        if flat_matrix[middle] == target:
            return True
        elif flat_matrix[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return False


print(search_matrix(matrix=[[1]], target=1))
