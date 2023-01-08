def categorize_box(length, width, height, mass):
    bulky, heavy, both, neither, bulky = False, False, False, False, False
    vol = length * height * width

    if vol >= 10**9 or length >= 10**4 or width >= 10**4 or height >= 10**4:
        bulky = True
    if mass >= 100:
        heavy = True

    if bulky and heavy:
        return 'Both'
    elif bulky and not heavy:
        return 'Bulky'
    elif heavy and not bulky:
        return 'Heavy'
    else:
        return 'Neither'


print(categorize_box(length = 1000, width = 35, height = 700, mass = 300))

