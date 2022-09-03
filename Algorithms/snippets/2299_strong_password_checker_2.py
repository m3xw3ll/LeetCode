def strong_password_checker_2(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    specials = '"!@#$%^&*()-+"'
    if len(password) < 8:
        return False
    for char in range(len(password)):
        if password[char].islower():
            has_lower = True
        if password[char].isupper():
            has_upper = True
        if password[char].isdigit():
            has_digit = True
        if password[char] in specials:
            has_special = True

    for char in range(1, len(password)):
        if password[char] == password[char-1]:
            return False
    if has_lower and has_upper and has_digit and has_special:
        return True
    return False


print(strong_password_checker_2('IloveLe3tcode!'))