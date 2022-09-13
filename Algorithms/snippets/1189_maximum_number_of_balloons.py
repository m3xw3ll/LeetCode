def max_number_of_balloons(text):
    chardict = {'b': 0, 'a': 0, 'l': 0, 'o':0, 'n':0}
    for char in text:
        if char in chardict:
            chardict[char] += 1
    chardict['l'] = chardict['l'] // 2
    chardict['o'] = chardict['o'] // 2

    return min(chardict.values())


print(max_number_of_balloons('loonbalxballpoon'))