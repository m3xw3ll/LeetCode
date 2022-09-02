def unique_morse_representations(words):
    codes = set()
    lookup = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..'
    }

    for word in words:
        wordmorse = ''
        for char in word:
            wordmorse += lookup[char]
        codes.add(wordmorse)
    return len(codes)


print(unique_morse_representations(["gin", "zen", "gig", "msg"]))
