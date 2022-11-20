def decode_message(key, message):
    dic = {' ': ' '}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    out = ''

    for k in key:
        if k not in dic:
            dic[k] = alpha[i]
            i += 1

    for m in message:
        out += dic[m]
    return out


print(decode_message(key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv"))
