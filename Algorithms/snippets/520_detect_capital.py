def detect_capital_use(word):
    return True if word.isupper() or \
                   word.islower() or \
                   (word[0].isupper() and word[1:].islower()) else False


print(detect_capital_use('FlaG'))