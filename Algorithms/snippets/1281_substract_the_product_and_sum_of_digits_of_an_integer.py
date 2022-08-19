import math


def substract_product_and_sum(n):
    sum_n = sum(int(i) for i in str(n))
    prod_n = math.prod(int(i) for i in str(n))
    return abs(sum_n - prod_n)


print(substract_product_and_sum(234))