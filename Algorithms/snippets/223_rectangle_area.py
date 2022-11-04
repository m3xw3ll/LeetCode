def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    a_area = abs(ax1 - ax2) * abs(ay1 - ay2)
    b_area = abs(bx1 - bx2) * abs(by1 - by2)

    left = max(ax1, bx1)
    right = min(ax2, bx2)
    bottom = max(ay1, by1)
    top = min(ay2, by2)

    print(left, right, bottom, top)

    if left < right and bottom < top:
        intersection = (right - left) * (top - bottom)
        return a_area + b_area - intersection
    return a_area + b_area


print(compute_area(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=3, by1=3, bx2=4, by2=4))
