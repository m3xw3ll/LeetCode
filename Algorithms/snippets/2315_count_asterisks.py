def count_asterisks(s):
    stack = []
    for i in s:
        if '|' not in stack:
            stack.append(i)
        elif '|' in stack and i == '|':
            stack.pop()
    return stack.count('*')


print(count_asterisks('l|*e*et|c**o|*de|'))