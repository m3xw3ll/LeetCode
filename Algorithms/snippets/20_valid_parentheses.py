def is_valid(s):
    lookup = {'(': ')',
              '{': '}',
              '[': ']'}
    stack = []
    for i in s:
        if i in lookup:
            stack.append(i)
        elif len(stack) == 0 or lookup[stack.pop()] != i:
            return False
    return len(stack) == 0


print(is_valid('()'))