def percentage_letter(s, letter):
    return int(s.count(letter) / len(s) * 100)


print(percentage_letter('foobar', 'o'))