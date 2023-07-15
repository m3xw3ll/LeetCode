def asteriod_collision(asteroids):
    stack = []
    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            if stack[-1] + a > 0:
                break
            elif stack[-1] + a < 0:
                stack.pop()
            else:
                stack.pop()
                break
        else:
            stack.append(a)
    return stack


print(asteriod_collision([5, 10, -5]))
