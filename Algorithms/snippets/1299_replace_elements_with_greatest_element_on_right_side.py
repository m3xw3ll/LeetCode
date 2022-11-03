def replace_elements(arr):
    r_max = -1
    for i in range(len(arr) - 1, -1, -1):
        tmp = arr[i]
        arr[i] = r_max
        if tmp > r_max:
            r_max = tmp
    return arr


print(replace_elements([17,18,5,4,6,1]))