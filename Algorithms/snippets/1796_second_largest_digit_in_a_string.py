def second_highest(s):
    nums = sorted(list(set([int(x) for x in s if x.isdigit()])))
    if len(nums) > 1:
        return nums[-2]
    return -1


print(second_highest('dfa12321afd'))
