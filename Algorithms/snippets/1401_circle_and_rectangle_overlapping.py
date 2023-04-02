def check_overlap(radius, x_center, y_center, x1, y1, x2, y2):
    nearest_x = max(x1, min(x2, x_center))
    nearest_y = max(y1, min(y2, y_center))
    dist_x = nearest_x - x_center
    dist_y = nearest_y - y_center

    return dist_x ** 2 + dist_y ** 2 <= radius ** 2


print(check_overlap(radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1))
