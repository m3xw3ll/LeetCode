def find_rotation(mat, target):
    cnt = 0
    while cnt < 3:
        if mat == target:
            return True
        mat = [list(x) for x in (zip(*mat[::-1]))]
        cnt += 1
    return False


print(find_rotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]))
