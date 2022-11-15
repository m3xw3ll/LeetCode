def three_consecutive_odds(arr):
    for i in range(len(arr) - 2):
        if all(x % 2 != 0 for x in arr[i:i + 3]):
            return True
    return False


print(three_consecutive_odds([2, 6, 4, 1]))