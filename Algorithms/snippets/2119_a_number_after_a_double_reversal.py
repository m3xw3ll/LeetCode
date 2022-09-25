def is_same_after_reversals(num):
    if num == 0:
        return True
    if str(num)[-1] == '0':
        return False
    return True



print(is_same_after_reversals(1800))