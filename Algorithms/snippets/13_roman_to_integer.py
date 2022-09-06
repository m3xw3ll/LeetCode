def roman_to_ing(s):
    lookup = {'I': 1,
              'IV': 4,
              'V': 5,
              'IX': 9,
              'X': 10,
              'XL': 40,
              'L': 50,
              'XC': 90,
              'C': 100,
              'CD': 400,
              'D': 500,
              'CM': 900,
              'M': 1000
              }
    out = 0
    curr = 0
    while curr < len(s):
        if s[curr:curr+2] in lookup:
            out += lookup[s[curr:curr+2]]
            curr += 2
        else:
            out += lookup[s[curr]]
            curr += 1
    return out


print(roman_to_ing('MCMXCIV'))
