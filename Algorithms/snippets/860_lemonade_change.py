def lemonade_change(bills):
    fives = 0
    tens = 0

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives > 0:
                fives -= 1
                tens += 1
            else:
                return False
        else:
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives > 2:
                fives -= 3
            else:
                return False
    return True


print(lemonade_change([5, 5, 10, 10, 20]))
