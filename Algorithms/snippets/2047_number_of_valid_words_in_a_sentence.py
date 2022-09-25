def count_valid_words(sentence):
    cnt = 0
    for word in sentence.split():
        is_valid = True
        num_hyphens = 0
        for i, c in enumerate(word):
            if c.isdigit() or (c in '!.,' and i != len(word) - 1) or (
                    c == '-' and (i == 0 or i == len(word) - 1 or not word[i + 1].isalpha())):
                is_valid = False
                break
            elif c == '-' and word[i+1].isalpha():
                num_hyphens += 1

        if is_valid and num_hyphens <= 1:
            cnt += 1

    return cnt


print(count_valid_words("cat and dog"))