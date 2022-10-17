def duplicate_zeros(arr):
    idx = 0
    while idx < len(arr):
        if arr[idx] == 0:
            arr.insert(idx, 0)
            arr.pop()
            idx += 2
        else:
            idx += 1
    return arr


print(duplicate_zeros([1,0,2,3,0,4,5,0]))