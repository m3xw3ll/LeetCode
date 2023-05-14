def count_seniors(details):
    age = [int(x[-4:-2]) for x in details]
    return len(list(filter(lambda x: x > 60, age)))


print(count_seniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
