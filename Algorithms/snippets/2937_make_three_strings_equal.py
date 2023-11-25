def find_minimum_operations(s1, s2, s3):
    if not (s1[0] == s2[0] == s3[0]):
        return -1
    else:
        idx = 0
        for s, ss, sss in zip(s1, s2, s3):
            if not s == ss == sss:
                break
            idx += 1
        return len(s1) + len(s2) + len(s3) - (idx * 3)


print(find_minimum_operations(s1="abc", s2="abb", s3="ab"))
