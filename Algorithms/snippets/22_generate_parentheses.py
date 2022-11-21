def generate_parenthesis(n):
    stack = []
    out = []

    def backtrack(n_open, n_close):
        if n_open == n_close == n:
            out.append(''.join(stack))
            return

        if n_open < n:
            stack.append('(')
            backtrack(n_open + 1, n_close)
            stack.pop()

        if n_close < n_open:
            stack.append(')')
            backtrack(n_open, n_close + 1)
            stack.pop()

    backtrack(0, 0)
    return out


print(generate_parenthesis(3))