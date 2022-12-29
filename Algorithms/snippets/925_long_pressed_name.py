def is_long_pressed_name(name, typed):
    ni = 0
    ti = 0
    while ni <= len(name) and ti < len(typed):
        if ni < len(name) and typed[ti] == name[ni]:
            ti += 1
            ni += 1
        elif typed[ti] == name[ni - 1] and ni != 0:
            ti += 1
        else:
            return False
    return ni == len(name) and ti == len(typed)


print(is_long_pressed_name(name = "alex", typed = "aaleex"))


