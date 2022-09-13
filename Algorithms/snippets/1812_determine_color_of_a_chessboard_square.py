def square_is_white(coordinates):
    if coordinates[0] in ['a', 'c', 'e', 'g'] and int(coordinates[1]) % 2 == 0:
        return True
    if coordinates[0] in ['b', 'd', 'f', 'h'] and int(coordinates[1]) % 2 != 0:
        return True
    return False


print(square_is_white('a1'))