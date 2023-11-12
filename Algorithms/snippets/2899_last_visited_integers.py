def last_visited_integers(words):
    nums = []
    out = []
    k = 0
    for i in words:
        if i.isdigit():
            nums.append(int(i))
            k = 0
        else:
            k += 1
            if k > len(nums):
                out.append(-1)
            else:
                out.append(nums[-k])
    return out


print(last_visited_integers(["1", "2", "prev", "prev", "prev"]))
