def get_encrypted_string(s, k):
    out = ''
    for i in range(len(s)):
        out += s[(i + k) % len(s)]
    return out


print(get_encrypted_string(s="dart", k=3))
