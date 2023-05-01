def rank_teams(votes):
    dic = {}

    for vote in votes:
        for idx, char in enumerate(vote):
            if char not in dic:
                dic[char] = [0] * len(vote)
            dic[char][idx] += 1

    names = sorted(dic.keys())
    return "".join(sorted(names, key=lambda x: dic[x], reverse=True))


print(rank_teams(votes=["ABC", "ACB", "ABC", "ACB", "ACB"]))
