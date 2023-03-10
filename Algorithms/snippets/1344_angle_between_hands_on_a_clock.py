def angle_clock(hour, minutes):
    minutes_hand = minutes * 6
    hour_hand = (hour % 12 * 30) + minutes / 60 * 30
    angle = abs(hour_hand - minutes_hand)
    return 360 - angle if angle > 180 else angle


print(angle_clock(hour=12, minutes=30))
