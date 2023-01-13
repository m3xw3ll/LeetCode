def mem_leak(memory1, memory2):
    i = 1
    while max(memory1, memory2) >= i:
        if memory1 >= memory2:
            memory1 -= i
        else:
            memory2 -= i
        i += 1
    return [i, memory1, memory2]


print(mem_leak(memory1=2, memory2=2))
