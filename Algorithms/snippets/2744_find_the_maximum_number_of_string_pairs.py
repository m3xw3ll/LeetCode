def maximum_number_of_string_pars(words):
    seen = []
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] == words[j][::-1] and words[i] not in seen:
                seen.append(words[i])
    return len(seen)


print(maximum_number_of_string_pars(["cd", "ac", "dc", "ca", "zz"]))
