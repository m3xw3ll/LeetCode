def find_relative_ranks(score):
    mydict = {}
    mylist = list(sorted(score, reverse=True))

    if len(score) >= 1:
        mydict[mylist[0]] = "Gold Medal"
    if len(score) >= 2:
        mydict[mylist[1]] = "Silver Medal"
    if len(score) >= 3:
        mydict[mylist[2]] = "Bronze Medal"
    print(mydict)
    out = list()
    for i in range(len(score)):
        if score[i] in mydict:
            out.append(mydict[score[i]])
        else:
            out.append(str(mylist.index(score[i]) + 1))
    return out


print(find_relative_ranks([5, 4, 3, 2, 1]))
