def decrypt(code, k):
    if k == 0:
        return [0] * len(code)
    tmp = code
    code = code * 2
    for i in range(len(tmp)):
        if k > 0:
            tmp[i] = sum(code[i+1:i+k+1])
        else:
            tmp[i] = sum(code[i+len(tmp)+k:i+len(tmp)])
    return tmp


print(decrypt(code=[5, 7, 1, 4], k=3))
