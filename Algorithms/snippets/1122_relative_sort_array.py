from collections import Counter


def relative_sort_array(arr1, arr2):
    c = Counter(arr1)
    out = list()
    tmp = list()
    for num in arr2:
        if num in c.keys():
            out.extend(num for i in range(c[num]))
    for i in arr1:
        if i not in out:
            tmp.append(i)
    sorted(tmp, reverse=True)
    return out + tmp


print(relative_sort_array(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
