def get_kth(lo, hi, k):
    def calc_pow(num, res):
        if num == 1:
            return res
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        res += 1
        return calc_pow(num, res)

    dic = {i: calc_pow(i, 0) for i in range(lo, hi + 1)}
    out = [k for k, v in sorted(dic.items(), key=lambda a:a[1])]
    return out[k-1]


print(get_kth(lo=12, hi=15, k=2))
