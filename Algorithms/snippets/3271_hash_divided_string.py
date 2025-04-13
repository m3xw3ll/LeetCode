def string_hash(s, k):
    result = ''
    for i in range(0, len(s), k):
        hash_sum = 0
        for j in s[i:i+k]:
            hash_sum += ord(j) - ord('a')
        hashed_char = hash_sum % 26
        result += chr(97+hashed_char)
    return result


print(string_hash(s="mxz", k=3))