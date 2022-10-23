def make_fancy_string(s):
    stack = []
    for char in s:
        if len(stack) > 1 and char == stack[-1] == stack[-2]:
            stack.pop()
        stack.append(char)
    return ''.join(stack)


print(make_fancy_string('leeetcode'))