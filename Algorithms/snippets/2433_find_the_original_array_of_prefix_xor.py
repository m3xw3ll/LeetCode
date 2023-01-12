def find_array(pref):
    return [pref[0]] + [pref[i-1] ^ pref[i] for i in range(1, len(pref))]


print(find_array([5, 2, 0, 3, 1]))
