def letter_case_permutation(s):
    out = list()

    def backtrack(sub, i):
        if len(sub) == len(s):
            out.append(sub)
        else:
            if s[i].isalpha():
                backtrack(sub + s[i].swapcase(), i + 1)
            backtrack(sub + s[i], i + 1)

    backtrack('', 0)
    return out


print(letter_case_permutation('a1b2'))
