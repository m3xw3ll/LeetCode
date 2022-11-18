def letter_combination(digits):
    lookup = {'2': 'abc',
              '3': 'def',
              '4': 'ghi',
              '5': 'jkl',
              '6': 'mno',
              '7': 'pqrs',
              '8': 'tuv',
              '9': 'wxyz'}

    out = list()

    def backtrack(i, curr):
        if len(digits) == len(curr):
            out.append(curr)
            return
        for c in lookup[digits[i]]:
            backtrack(i+1, curr + c)

    if digits:
        backtrack(0, '')
    return out


print(letter_combination('23'))