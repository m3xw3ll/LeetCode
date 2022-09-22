def int_to_roman(num):
    lookup = {'M': 1000,
              'CM': 900,
              'D': 500,
              'CD': 400,
              'C': 100,
              'XC': 90,
              'L': 50,
              'XL': 40,
              'X': 10,
              'IX': 9,
              'V': 5,
              'IV': 4,
              'I': 1,
              }

    out = ''
    for char, value in lookup.items():
        while num >= value:
            out += char
            num -= value
    return out


print(int_to_roman(3))