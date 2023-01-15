def closet_target(words, target, start_idx):
    if target not in words:
        return -1

    pos = float('inf')
    for i in range(len(words)):
        if words[i] == target:
            pos = min(pos, abs(i - start_idx), len(words) - abs(i - start_idx))
    return pos


print(closet_target(words=["hello", "i", "am", "leetcode", "hello"], target="hello", start_idx=1))
