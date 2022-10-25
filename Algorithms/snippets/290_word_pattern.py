def word_pattern(pattern, s):
    s = s.split()
    if len(pattern) != len(s):
        return False

    dic = {}
    for a, b in zip(pattern, s):
        if a in dic and dic[a] != b:
            return False
        dic[a] = b
    if len(set(dic.keys())) != len(set(dic.values())):
        return False
    return True



print(word_pattern('abba', 'cat dog dog cat'))