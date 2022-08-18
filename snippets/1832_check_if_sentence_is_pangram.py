import string


def check_if_pangram(sentence):
    s = set(sentence)
    return s.issuperset(string.ascii_lowercase)


print(check_if_pangram('leetcode'))