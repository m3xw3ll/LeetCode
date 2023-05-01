def find_the_prefix_common_array(A, B):
    n = len(A)
    out = []
    for i in range(n):
        out.append(len(set(A[:i + 1]) & set(B[:i + 1])))
    return out


print(find_the_prefix_common_array(A=[2, 3, 1], B=[3, 1, 2]))
