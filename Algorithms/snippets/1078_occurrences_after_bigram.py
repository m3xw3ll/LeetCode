def find_occurrences(text, first, second):
    out = []
    text = text.split()
    for i in range(len(text) - 2):
        if text[i] == first and text[i+1] == second:
            out.append(text[i+2])
    return out


print(find_occurrences(text='alice is a good girl she is a good student', first='a', second='good'))