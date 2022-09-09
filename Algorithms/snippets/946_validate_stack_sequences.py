def validate_stack_sequences(pushed, popped):
    i = 0
    j = 0
    stack = []

    while i < len(pushed) and j < len(popped):
        stack.append(pushed[i])
        i += 1

        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1

    if stack:
        return False
    return True


print(validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
