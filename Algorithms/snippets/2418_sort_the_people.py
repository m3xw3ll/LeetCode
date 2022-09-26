def sort_people(names, heights):
    test = sorted(list(zip(names, heights)), key=lambda x:x[1], reverse=True)
    return [i[0] for i in test]


print(sort_people(["Mary","John","Emma"], [180,165,170]))