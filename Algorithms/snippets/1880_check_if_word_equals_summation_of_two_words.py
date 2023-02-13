def is_sum_equal(first_word, second_word, target_word):
    first_word = ''.join(str(ord(char) - 97) for char in first_word)
    second_word = ''.join(str(ord(char) - 97) for char in second_word)
    target_word = ''.join(str(ord(char) - 97) for char in target_word)
    return int(first_word) + int(second_word) == int(target_word)


print(is_sum_equal(first_word="j", second_word="j", target_word="bi"))
