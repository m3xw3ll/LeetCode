def is_prefix_string(s, words):
    tmp = ''
    for word in words:
        tmp += word
        if tmp == s:
            return True
    return False


print(is_prefix_string('iloveleetcode', ["i", "love", "leetcode", "apples"]))
