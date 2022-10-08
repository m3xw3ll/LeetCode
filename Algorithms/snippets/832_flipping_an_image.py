def flip_and_invert_image(image):
    for i in range(len(image)):
        start = 0
        end = len(image[i]) - 1
        while start <= end:
            image[i][start], image[i][end] = image[i][end] ^ 1, image[i][start] ^ 1
            start += 1
            end -= 1
    return image


print(flip_and_invert_image([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
