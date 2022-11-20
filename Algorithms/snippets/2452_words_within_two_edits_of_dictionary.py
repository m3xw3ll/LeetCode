def two_edit_words(queries, dictionary):
    out = list()
    for q in queries:
        for d in dictionary:
            cnt = 0
            for x, y, in zip(q, d):
                if x != y:
                    cnt += 1
                    if cnt > 2:
                        break
            if cnt <= 2:
                out.append(q)
                break
    return out


print(two_edit_words(queries=["word", "note", "ants", "wood"], dictionary=["wood", "joke", "moat"]))
