def number_of_lines(widths, s):
    dic = dict(zip([chr(i) for i in range(97, 123)], widths))
    l_number = 1
    l_width = 0
    for i in s:
        if l_width + dic[i] <= 100:
            l_width += dic[i]
        else:
            l_number += 1
            l_width = dic[i]

    return [l_number, l_width]


print(number_of_lines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                      'bbbcccdddaaa'))