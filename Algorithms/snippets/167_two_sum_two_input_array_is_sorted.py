def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        if numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1


print(two_sum(numbers=[2, 7, 11, 15], target=9))
