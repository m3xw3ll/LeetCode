def maximum_units(box_types, truck_size):
    cnt = 0
    box_types.sort(key=lambda x: x[1], reverse=1)
    for i, j in box_types:
        i = min(i, truck_size)
        cnt += i * j
        truck_size -= i
        if truck_size == 0:
            break
    return cnt



print(maximum_units(box_types=[[5, 10], [2, 5], [4, 7], [3, 9]], truck_size=10))
