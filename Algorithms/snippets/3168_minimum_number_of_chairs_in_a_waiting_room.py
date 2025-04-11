def minimum_chairs(s):
    num_people = 0
    max_people = 0
    for i in s:
        if i == 'E':
            num_people += 1
        else:
            num_people -= 1
        max_people = max(max_people, num_people)
    return max_people

print(minimum_chairs("ELELEEL"))