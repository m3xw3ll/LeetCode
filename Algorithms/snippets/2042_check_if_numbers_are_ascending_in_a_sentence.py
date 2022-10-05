def are_numbers_ascending(s):
    numbers = [int(x) for x in s.split() if x.isdigit()]
    return all(i < j for i, j in zip(numbers, numbers[1:]))


print(are_numbers_ascending('1 box has 3 blue 4 red 6 green and 12 yellow marbles'))