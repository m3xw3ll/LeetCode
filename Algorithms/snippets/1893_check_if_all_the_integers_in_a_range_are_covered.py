def is_covered(ranges, left, right):
    for i in range(left, right + 1):
        for l, r in ranges:
            found = False
            if l <= i <= r:
                found = True
                break
        if not found:
            return False
    return True


print(is_covered(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5))
