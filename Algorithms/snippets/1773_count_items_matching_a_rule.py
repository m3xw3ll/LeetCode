def count_matches(items, rulekey, rulevalue):
    lookup = {
        'type': 0,
        'color': 1,
        'name': 2
    }
    cnt = 0
    for item in items:
        if item[lookup[rulekey]] == rulevalue:
            cnt += 1
    return cnt


print(count_matches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], rulekey = "color", rulevalue = "silver"))