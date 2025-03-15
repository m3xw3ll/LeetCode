def find_valid_pair(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in range(len(s) - 1):
        first, second = s[i:i+2]
        if first != second and d[first] == int(first) and d[second] == int(second):
            return first + second
    return ""


print(find_valid_pair("2523533"))
