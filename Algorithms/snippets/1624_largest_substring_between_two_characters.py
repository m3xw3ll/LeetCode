def max_length_between_equal_characters(s):
    dic = {}
    dist = -1

    for idx, char in enumerate(s):
        if char not in dic:
            dic[char] = idx
        else:
            dist = max(dist, idx - dic[char] - 1)
    return dist


print(max_length_between_equal_characters('ojdncpvyneq'))