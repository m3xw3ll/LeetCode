def next_greatest_letter(letters, target):
    if max(letters) <= target:
        return min(letters)
    for letter in letters:
        if letter > target:
            return letter


print(next_greatest_letter(["c","f","j"], 'c'))