def find_the_distance_value(arr1, arr2, d):
    cnt = 0

    def checker(x, y, d):
        return abs(x - y) > d

    for a in arr1:
        valid = True
        for b in arr2:
            if not checker(a, b, d):
                valid = False
        if valid:
            cnt += 1
    return cnt


print(find_the_distance_value(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
