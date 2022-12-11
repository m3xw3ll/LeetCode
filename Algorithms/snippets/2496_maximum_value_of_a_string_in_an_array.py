def maximum_value(strs):
    ma = 0
    for s in strs:
        if s.isdigit():
            ma = max(ma, int(s))
        else:
            ma = max(ma, len(s))
    return ma


print(maximum_value(["alic3", "bob", "3", "4", "00000"]))
