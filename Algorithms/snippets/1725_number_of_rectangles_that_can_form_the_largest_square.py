def count_good_rectangles(rectangles):
    sides = list()
    for rect in rectangles:
        sides.append(min(rect))
    return sides.count(max(sides))


print(count_good_rectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
