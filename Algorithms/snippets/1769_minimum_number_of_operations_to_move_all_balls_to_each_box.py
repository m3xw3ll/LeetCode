def min_operations(boxes):
    out = [0] * len(boxes)
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if boxes[j] == '1':
                out[i] += abs(j-i)

    return out


print(min_operations('001011'))