def find_complement(num):
    num = bin(num)[2:]
    comp = []
    for i in num:
        if i == '1':
            comp.append('0')
        else:
            comp.append('1')
    return int(''.join(comp), 2)


print(find_complement(5))