def clear_digits(s):
    stack = []
    for c in s:
        if c.isdigit():
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)


print(clear_digits("abc"))
