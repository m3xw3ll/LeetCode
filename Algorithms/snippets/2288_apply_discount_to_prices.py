def discount_prices(sentence, discount):
    s = sentence.split()
    out = list()
    for word in s:
        if word[0] == '$' and word[1:].isdigit():
            out.append(f'${int(word[1:]) * (1 - (discount / 100)):.2f}')
        else:
            out.append(word)
    return ' '.join(out)


print(discount_prices(sentence="there are $1 $2 and 5$ candies in the shop", discount=50))
