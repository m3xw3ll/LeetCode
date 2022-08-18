def min_time_to_type(word):
    time = len(word)
    prev = 'a'
    for character in word:
        val = (ord(character) - ord(prev)) % 26
        time += min(val, abs(26-val))
        prev = character
    return time


print(min_time_to_type('abc'))