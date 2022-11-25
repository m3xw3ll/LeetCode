def can_tree_parts_equal_sum(arr):
    S = sum(arr)
    cumsum = 0
    target = S // 3
    cnt = 0

    if S % 3 != 0:
        return False

    for i in arr:
        cumsum += i
        if cumsum == target:
            cnt += 1
            cumsum = 0
        if cnt == 3:
            return True
    return False


print(can_tree_parts_equal_sum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
