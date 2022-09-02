def remove_stars(s):
    stack = []
    for i in s:
        if i == '*':
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)


print(remove_stars('leet**cod*e'))