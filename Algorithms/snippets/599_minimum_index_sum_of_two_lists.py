def find_restaurant(list1, list2):
    out = []
    dummy = float('inf')
    dups = [x for x in list1 if x in list2]
    for word in dups:
        idx_sum = list1.index(word) + list2.index(word)
        if idx_sum < dummy:
            out = [word]
            dummy = idx_sum
        elif idx_sum == dummy:
            out.append(word)
    return out


print(find_restaurant(["happy","sad","good"], list2 = ["sad","happy","good"]))
