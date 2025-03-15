def stable_mountains(height, threshold):
    stables = list()
    for i in range(1, len(height)):
        if height[i-1] > threshold:
            stables.append(i)
    return stables


print(stable_mountains(height=[1, 2, 3, 4, 5], threshold=2))
