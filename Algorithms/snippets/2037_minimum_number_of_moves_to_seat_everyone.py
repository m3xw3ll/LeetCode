def min_moves_to_seat(seats, students):
    out = 0

    for x, y in zip(sorted(seats), sorted(students)):
        out += abs(x-y)
    return out


print(min_moves_to_seat([3, 1, 5], [2, 7, 4]))
