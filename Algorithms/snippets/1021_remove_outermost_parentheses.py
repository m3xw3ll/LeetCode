def remove_outer_parentheses(s):
    out = list()
    open = 0
    for i in s:
        if i == '(' and open > 0:
            out.append(i)
        if i == ')' and open > 1:
            out.append(i)
        open += 1 if i == '(' else - 1
    return ''.join(out)


print(remove_outer_parentheses("(()())(())"))