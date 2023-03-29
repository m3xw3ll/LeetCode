def k_items_with_maximum_sum(num_ones, num_zeros, num_neg_ones, k):
    if k < num_ones:
        return k
    elif k <= num_ones + num_zeros:
        return num_ones
    else:
        return num_ones - (k - (num_ones + num_zeros))


print(k_items_with_maximum_sum(num_ones = 6, num_zeros = 6, num_neg_ones = 6, k = 13))
