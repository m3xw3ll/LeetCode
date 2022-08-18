def self_dividing_numbers(left, right):
    output = []
    cleaned = []
    for i in range(left, right+1, 1):
        if '0' not in str(i):
            cleaned.append(str(i))
    for j in cleaned:
        c = 0
        for k in j:
            if int(j) % int(k) == 0:
                c += 1
        if c == len(str(j)):
            output.append(j)
    return output


print(self_dividing_numbers(1, 22))