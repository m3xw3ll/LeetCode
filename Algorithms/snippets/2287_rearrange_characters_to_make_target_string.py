def rearrange_characters(s, target):
    out = list()
    for i in range(len(set(target))):
        s_cnt = s.count(target[i])
        t_cnt = target.count(target[i])

        if t_cnt <= s_cnt:
            out.append(s_cnt // t_cnt)
        else:
            return 0
    return min(out)


print(rearrange_characters(s="ilovecodingonleetcode", target="code"))
