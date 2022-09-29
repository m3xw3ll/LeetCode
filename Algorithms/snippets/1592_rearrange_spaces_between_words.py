def reorder_spaces(text):
    cnt = text.count(' ')
    words = text.split()

    if len(words) > 1:
        btw = cnt // (len(words) - 1)
        end = cnt % (len(words) -1)
    else:
        btw = 0
        end = cnt

    return (" " * btw).join(words) + " " * end


print(reorder_spaces(" practice   makes   perfect"))
