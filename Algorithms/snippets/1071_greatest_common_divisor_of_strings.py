import math


def gcd_of_strings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ''
    else:
        split = math.gcd(len(str1), len(str2))
        return str1[:split]


print(gcd_of_strings(str1 = "ABCABC", str2 = "ABC"))