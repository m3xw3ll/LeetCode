def make_good(s):
    stack = []
    for i in s:
        if stack and i.swapcase() == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)


print(make_good('abBAcC'))
