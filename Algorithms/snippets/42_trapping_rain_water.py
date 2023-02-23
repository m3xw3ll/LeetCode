def trap(height):
    left = 0
    right = len(height) - 1
    water = 0

    max_left = height[left]
    max_right = height[right]

    while left < right:
        if height[left] <= height[right]:
            left += 1
            max_left = max(max_left, height[left])
            water += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            water += max_right - height[right]
    return water


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
