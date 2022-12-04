def is_circular_sentence(sentence):
    sentence = sentence.split()
    if sentence[-1][-1] != sentence[0][0]:
        return False
    for i in range(0, len(sentence) - 1):
        if sentence[i][-1] != sentence[i+1][0]:
            return False
    return True


print(is_circular_sentence("leetcode"))