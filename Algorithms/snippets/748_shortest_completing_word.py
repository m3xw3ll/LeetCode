def shortest_completing_word(license_plate, words):
    lp = [x.lower() for x in license_plate if x.isalpha()]
    words = sorted(words, key=len)

    for word in words:
        for i in range(len(lp)):
            if word.count(lp[i]) < lp.count(lp[i]):
                break
            if i == len(lp) - 1:
                return word


print(shortest_completing_word(license_plate="1s3 PSt", words=["step", "steps", "stripe", "stepple"]))
