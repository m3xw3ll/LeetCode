def remove_duplicates(s):
    stack = []
    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


print(remove_duplicates('abbaca'))