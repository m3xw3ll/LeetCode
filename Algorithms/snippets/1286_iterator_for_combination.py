class CombinationIterator:
    def __init__(self, characters, combination_length):
        def backtrack(start, curr_combination):
            if len(curr_combination) == combination_length:
                self.combinations_list.append(''.join(curr_combination[:]))
                return

            for i in range(start, len(characters)):
                curr_combination.append(characters[i])
                backtrack(i + 1, curr_combination)
                curr_combination.pop()

        self.combinations_list = []
        self.idx = 0
        backtrack(0, [])

    def next(self):
        nex_comb = self.combinations_list[self.idx]
        self.idx += 1
        return nex_comb

    def has_next(self):
        return True if self.idx < len(self.combinations_list) else False


if __name__ == '__main__':
    ci = CombinationIterator('abc', 2)
    print(ci.next())
    print(ci.has_next())
    print(ci.next())
    print(ci.has_next())
    print(ci.next())
    print(ci.has_next())