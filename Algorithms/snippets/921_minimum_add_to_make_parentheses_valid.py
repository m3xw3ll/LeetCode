def min_add_to_make_valid(s):
    lookup = {')': '('}
    stack = []
    i = 0

    while i < len(s):
        if stack and stack[-1] == lookup.get(s[i], None):
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
    return len(stack)


print(min_add_to_make_valid('()))(('))