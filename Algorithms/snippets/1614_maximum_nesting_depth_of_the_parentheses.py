def max_depth(s):
    stack = []
    max_depth = 0
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            max_depth = max(max_depth, len(stack))
            stack.pop()
    return max_depth


print(max_depth('(1+(2*3)+((8)/4))+1'))