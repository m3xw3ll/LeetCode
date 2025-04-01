def count_key_changes(s):
    cnt = 0
    for i in range(len(s) - 1):
        if not s[i].lower() == s[i+1].lower():
            cnt += 1
    return cnt


print(count_key_changes('AaAaAaaA'))