def to_hex(num):
    lookup = {0: '0',
              1: '1',
              2: '2',
              3: '3',
              4: '4',
              5: '5',
              6: '6',
              7: '7',
              8: '8',
              9: '9',
              10: 'a',
              11: 'b',
              12: 'c',
              13: 'd',
              14: 'e',
              15: 'f'
              }

    hexa = ''
    if num < 0:
        num = (2 ** 32) + num
    if num == 0:
        return 0
    while num > 0:
        rem = num % 16
        hexa = lookup[rem] + hexa
        num = num // 16
    return hexa


print(to_hex(26))