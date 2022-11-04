def title_to_number(column_title):
    s = 0
    for i in column_title:
        s = s * 26 + (ord(i)) - ord('A') + 1
    return s


print(title_to_number('ZY'))